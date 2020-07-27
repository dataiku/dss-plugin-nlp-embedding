import json
import requests
import shutil
import gzip
import os
from pathlib import Path
import tarfile
import io
import zipfile
from macro.model_configurations import MODEL_CONFIFURATIONS
import time
from transformers.file_utils import (S3_BUCKET_PREFIX,
                                    CLOUDFRONT_DISTRIB_PREFIX,
                                    hf_bucket_url)
from .model_configurations import MODEL_CONFIFURATIONS


WORD2VEC_BASE_URL = "http://vectors.nlpl.eu/repository/20/{}.zip"
FASTTEXT_BASE_URL = "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.{}.300.vec.gz"
HG_FILENAMES = ["pytorch_model.bin","config.json","vocab.txt"]

class BaseDownloader(object):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        self.folder = folder
        self.proxy = proxy
        self.progress_callback = progress_callback
        self.language = macro_inputs["language"]
        self.embedding_model = macro_inputs["embedding_model"]
        self.model_params = MODEL_CONFIFURATIONS[self.embedding_model]
        self.model_id = self.embedding_model + '-' + self.language
        self.archive_name = ''



    def get_stream(self, download_link):
        response = requests.get(download_link, stream=True, proxies=self.proxy)
        return response

    def download_plain(self, response, bytes_so_far=0):
        #Download plain files
        total_size = self.get_file_size(response)
        update_time = time.time()
        with self.folder.get_writer(self.archive_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    bytes_so_far += len(chunk)
                    percent = int(float(bytes_so_far) / total_size * 100)
                    update_time = self.update_percent(percent, update_time)
                    w.write(chunk)
        return bytes_so_far

    def download_gz(self, response, bytes_so_far=0):
        #Download .ga files
        total_size = self.get_file_size(response)
        update_time = time.time()
        destination_writer = self.folder.get_writer(self.archive_name)

        #Write .gz file to folder
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:  # filter out keep-alive new chunks
                bytes_so_far += len(chunk)
                percent = int(float(bytes_so_far) / total_size * 95)
                update_time = self.update_percent(percent, update_time)
                destination_writer.write(chunk)
        destination_writer.close()

        #Unzip file
        with self.folder.get_writer(self.model_id) as f_out, self.folder.get_download_stream(self.archive_name) as f_in:
            shutil.copyfileobj(gzip.open(f_in), f_out)
        
        #Remove the .gz file
        self.folder.delete_path(self.archive_name)
        return bytes_so_far

    def download_tar_gz(self, response, bytes_so_far=0):
        #Download .tar files
        total_size = self.get_file_size(response)
        update_time = time.time()
        with self.folder.get_writer(self.archive_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    bytes_so_far += len(chunk)
                    percent = int(float(bytes_so_far) / total_size * 95)
                    update_time = self.update_percent(percent, update_time)
                    w.write(chunk)
        #Untar file
        with self.folder.get_download_stream(self.archive_name) as f_in:
            with tarfile.open(fileobj=io.BytesIO(f_in.read())) as tar:
                members = tar.getmembers()
                for member in members:
                    if member.isfile():
                        with self.folder.get_writer(member.name) as f_out:
                            shutil.copyfileobj(tar.extractfile(member),f_out)
            self.folder.delete_path(self.archive_name)
        return bytes_so_far

    def download_zip(self, response, bytes_so_far = 0):
        #Download .zip files
        total_size = self.get_file_size(response)
        update_time = time.time()
        with self.folder.get_writer(self.archive_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    bytes_so_far += len(chunk)
                    percent = int(float(bytes_so_far) / total_size * 95)
                    update_time = self.update_percent(percent, update_time)
                    w.write(chunk)
        #Unzip file
        with self.folder.get_download_stream(self.archive_name) as f_in:
            with zipfile.ZipFile(io.BytesIO(f_in.read())) as fzip:
                if self.embedding_model == "word2vec":
                    archive_name = "model.bin"
                elif self.embedding_model == "glove":
                    archive_name = fzip.namelist()[0]
                else:
                    raise NotImplementedError()
                with fzip.open(archive_name) as fzip_file, self.folder.get_writer(self.model_id) as f_out:
                    shutil.copyfileobj(fzip_file, f_out)
            self.folder.delete_path(self.archive_name)  
        return bytes_so_far  

    def get_file_size(self,response):
        total_size = int(response.headers.get('content-length'))
        return total_size

    def update_percent(self,percent, last_update_time):
            new_time = time.time()
            if (new_time - last_update_time) > 5:
                self.progress_callback(percent)
                return new_time
            else:
                return last_update_time

    def get_download_link(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()




class Word2vecDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)   
        self.archive_name = self.language + '/' + self.embedding_model + '/'   
        if self.language == "english":
            self.archive_name += self.model_id + ".bin.gz"
        else:
            self.archive_name += self.model_id + ".zip"
            
    def get_gdrive_stream(self, download_link):
        id_gdrive = self.model_params["download_info"][self.language]["id_gdrive"]
        session = requests.Session()
        response = session.get(download_link, params={'id': id_gdrive} , stream=True, proxies=self.proxy) 
        token = self.__get_confirm_token(response)

        if token:
            params = {'id': id_gdrive, 'confirm': token}
            response = session.get(download_link, params=params, stream=True, proxies=self.proxy)
        else:
            raise RuntimeError("Google Drive Token could not be verified.")

        return response   

    def __get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None   

    def get_download_link(self):
        if self.language == "english":
            return self.model_params["download_info"][self.language]["model_link"]
        else:
            model_id = self.model_params["download_info"][self.language]["model_id"]
            return WORD2VEC_BASE_URL.format(model_id)

    def run(self):
        if self.language == "english":
            download_link = self.get_download_link()
            response = self.get_gdrive_stream(download_link)
            self.download_gz(response)
        else:
            download_link = self.get_download_link()
            response = self.get_stream(download_link)
            self.download_zip(response) 
        



class FasttextDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)
        self.archive_name = self.language + '/' + self.embedding_model + '/' + self.model_id + ".gz"

    def get_download_link(self):
        return FASTTEXT_BASE_URL.format(self.model_params["download_info"][self.language])

    def run(self):
        download_link = self.get_download_link()
        response = self.get_stream(download_link)
        self.download_gz(response)

    



class GloveDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)
        self.archive_name = self.model_id + ".zip"

    def get_download_link(self): 
        return self.model_params["download_info"][self.language]["model_link"]
        
    def run(self):
        download_link = self.get_download_link()
        response = self.get_stream(download_link)
        self.download_zip(response)
        

class ElmoDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)
        self.archive_name = self.model_id + ".tar.gz"
    
    def get_download_link(self): 
        return self.model_params["download_info"][self.language]["model_link"]
    
    def run(self):
        download_link = self.get_download_link()
        response = self.get_stream(download_link)
        self.download_tar_gz(response)




class UseDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)
        self.archive_name = self.model_id + ".tar.gz"

    def get_download_link(self): 
        return self.model_params["download_info"][self.language]["model_link"]  

    def run(self):
        download_link = self.get_download_link()
        response = self.get_stream(download_link)
        self.download_tar_gz(response)



class HuggingFaceDownloader(BaseDownloader):
    def __init__(self,folder,macro_inputs,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,macro_inputs,proxy,progress_callback)
        self.macro_inputs = macro_inputs
        self.model_shortcut_name = self.macro_inputs["transformer_shortcut_name"]
        
    def run(self):
        bytes_so_far = 0
        for filename in HG_FILENAMES:
            self.archive_name = filename
            download_link = self.get_download_link(filename)         
            response = self.get_stream(download_link)
            bytes_so_far = self.download_plain(response, bytes_so_far)

    def get_file_size(self, response=None):
        total_size = 0
        for filename in HG_FILENAMES:
            download_link = self.get_download_link(filename)
            response = self.get_stream(download_link)
            total_size += int(response.headers.get('content-length'))
        return total_size


    def get_download_link(self,filename): 
        return hf_bucket_url(self.model_shortcut_name,filename)