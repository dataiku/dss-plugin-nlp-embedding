import json
import requests
import shutil
import gzip
import os
import tempfile
import tarfile
import tensorflow as tf
import tensorflow_hub as hub

class word2vec_downloader():
    def __init__(self,folder,language,params):
        self.folder = folder
        self.language = language
        self.file_name = "word2vec_" + str(self.language)
        self.params = params[self.file_name]["params"]
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


class fasttext_downloader():
    def __init__(self,folder,language,params):
        self.folder = folder
        self.language = language   
        self.file_name = "fasttext-" + str(self.language)
        self.params = params[self.file_name]["params"]


    def get_stream(self):
        response = requests.get(self.params["link_model"], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.file_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)


class glove_downloader():
    def __init__(self,folder,language,params):
        self.folder = folder
        self.language = language   
        self.file_name = "glove-" + str(self.language)
        self.params = params[self.file_name]["params"]
        self.archive_name = ""


    def get_stream(self):
        response = requests.get(self.params["link_model"], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.file_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)

class elmo_downloader():
    def __init__(self,folder,language,params):
        self.folder = folder
        self.language = language   
        self.file_name = "elmo-" + str(self.language)
        self.params = params[self.file_name]["params"]


    def get_stream(self):
        response = requests.get(self.params["link_model"], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.file_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)


class huggingface_downloader():
    def __init__(self,folder,language,params):
        self.folder = folder
        self.language = language   
        self.file_name = "elmo-" + str(self.language)
        self.params = params[self.file_name]["params"]
        self.archive_name = ""


    def get_stream(self):
        response = requests.get(self.params["link_model"], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.file_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)