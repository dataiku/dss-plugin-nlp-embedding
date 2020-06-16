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

class BaseDownloader(object):
    def __init__(self,folder,model_params,proxy,progress_callback):
        self.folder = folder
        self.model_params = model_params
        self.proxy = proxy
        self.progress_callback = progress_callback
        self.archive_name = ''



    def get_stream(self):
        download_link = self.get_download_link()
        response = requests.get(download_link, stream=True, proxies=self.proxy)
        return response

    def download(self):
        bytes_so_far = 0
        response = self.get_stream()
        total_size = self.get_file_size(response)
        update_time = time.time()
        with self.folder.get_writer(self.archive_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    bytes_so_far += len(chunk)
                    percent = int(float(bytes_so_far) / total_size * 100)
                    update_time = self.update_percent(percent, update_time)
                    w.write(chunk)

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




class Word2vecDownloader(BaseDownloader):
    def __init__(self,folder,model_params,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,model_params,proxy,progress_callback)
        self.language = model_params["language"]
        self.model_id = 'word2vec-' + self.language
        self.archive_name = self.model_id + ".bin.gz"


    def get_gdrive_stream(self,link = "link_model"):
        id_gdrive = model_params[self.language]["id_gdrive"]
        session = requests.Session()
        download_link = self.get_download_link()
        response = session.get(download_link, params={'id': id_gdrive , stream=True, proxies=self.proxy) 
        token = self.__get_confirm_token(response)

        if token:
            params = {'id': self.model_params["params"]["id_gdrive"], 'confirm': token}
            response = session.get(self.model_params["params"]["link_model"], params=params, stream=True, proxies=self.proxy)
        else:
            raise RuntimeError("Google Drive Token could not be verified.")

        return response

    def download(self):
        bytes_so_far = 0
        response = self.get_stream()
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

    def __get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None   

    def get_download_link(self):
        pass



class FasttextDownloader(BaseDownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,model_id,proxy,progress_callback)


class GloveDownloader(BaseDownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,model_id,proxy,progress_callback)
        self.archive_name = self.model_id + ".zip"

    def download(self):
        #Donwload .zip file
        bytes_so_far = 0
        response = self.get_stream()
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
                archive_name = fzip.namelist()[0]
                with fzip.open(archive_name) as fzip_file, self.folder.get_writer(self.model_id) as f_out:
                    shutil.copyfileobj(fzip_file, f_out)
            self.folder.delete_path(self.archive_name)       


class Tfhubownloader(BaseDownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,model_id,proxy,progress_callback)
        self.archive_name = self.model_id + ".tar.gz"

    def download(self):
        #Donwload .tar file
        bytes_so_far = 0
        response = self.get_stream()
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
        

class ElmoDownloader(Tfhubownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        Tfhubownloader.__init__(self,folder,model_id,proxy,progress_callback)

class UseDownloader(Tfhubownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        Tfhubownloader.__init__(self,folder,model_id,proxy,progress_callback)        


class HuggingFaceDownloader(BaseDownloader):
    def __init__(self,folder,model_id,proxy,progress_callback):
        BaseDownloader.__init__(self,folder,model_id,proxy,progress_callback)
        self.archive_name = {
            "link_model": "pytorch_model.bin",
            "link_config": "config.json",
            "link_vocab": "vocab.txt"
        }

    def download(self):
        bytes_so_far = 0
        total_size = self.get_file_size()
        update_time = time.time()
        for parameter in self.model_params["params"].keys():
            response = self.get_stream(parameter)
            with self.folder.get_writer(self.archive_name[parameter]) as w:
                for chunk in response.iter_content(chunk_size=100000):
                    if chunk:
                        bytes_so_far += len(chunk)
                        percent = int(float(bytes_so_far) / total_size * 95)
                        update_time = self.update_percent(percent, update_time)
                        w.write(chunk)

    def get_file_size(self):
        total_size = 0
        for parameter in self.model_params["params"].keys():
            response = self.get_stream(parameter)
            total_size += int(response.headers.get('content-length'))
        return total_size