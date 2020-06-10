import json
import requests
import shutil
import gzip
import os
import tempfile
import tarfile
import tensorflow as tf
import tensorflow_hub as hub


class BaseDownloader(object):
    def __init__(self,folder,model_id,model_params):
        self.folder = folder
        self.model_params = model_params
        self.model_id = model_id


    def get_stream(self,link = self.params["params"]["link_model"]):
        response = requests.get(link, stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.model_id) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)

class Word2vecDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)
        self.archive_name = "GoogleNews-vectors-negative300.bin.gz"


    def get_stream(self):
        session = requests.Session()
        response = session.get(self.params["link_model"], params={'id': self.params["id_model"]}, stream=True)
        token = self.__get_confirm_token(response)

        if token:
            params = {'id': self.params["id_model"], 'confirm': token}
            response = session.get(self.params["link_model"], params=params, stream=True)
        else:
            raise RuntimeError("Google Drive Token could not be verified.")

        return response

    def download(self):
        response = self.get_stream()
        destination_writer = self.folder.get_writer()

        #Write .gz file to folder
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:  # filter out keep-alive new chunks
                destination_writer.write(chunk)
        destination_writer.close()

        #Unzip file
        with self.folder.get_writer(self.file_name) as f_out, self.folder.get_download_stream(self.archive_name) as f_in:
            shutil.copyfileobj(gzip.open(f_in), f_out)
        
        #Remove the .gz file
        self.folder.delete_path(self.gdrive_file_name)

    def __get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None   


class FasttextDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)



class GloveDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)


class ElmoDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)

class UseDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)

class HuggingFaceDownloader(BaseDownloader):
    def __init__(self,folder,model_id,model_params):
        BaseDownloader.__init__(self,folder,model_id,model_params)

    def download(self):
        for file_name, file_link in self.model_params["params"].items():
            response = self.get_stream(file_link)
            with self.folder.get_writer(file_name) as w:
                for chunk in response.iter_content(chunk_size=100000):
                    if chunk:
                        w.write(chunk)