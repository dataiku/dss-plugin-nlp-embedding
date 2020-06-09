from dataiku.customrecipe import *
import json
import requests
import shutil
import gzip
import os

class word2vec_downloader():
    def __init__(self,folder,language):
        self.folder = folder
        self.language = language
        self.file_name = "word2vec_" + str(self.language)
        self.params = json.load(os.path.join(get_recipe_resource(),"models_download_links.json"))[self.file_name]
        self.gdrive_file_name = "GoogleNews-vectors-negative300.bin.gz"


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
        with self.folder.get_writer(self.file_name) as f_out, self.folder.get_download_stream(self.gdrive_file_name) as f_in:
            shutil.copyfileobj(gzip.open(f_in), f_out)
        
        #Remove the .gz file
        self.folder.delete_path(self.gdrive_file_name)

    def __get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None   


class fasttext_downloader():
    def __init__(self,folder,language):
        self.folder = folder
        self.language = language   
        self.file_name = "fasttext_" + str(self.language)
        print("heeeere: ")
        print(get_recipe_resource())
        self.params = json.load(os.path.join(get_recipe_resource(),"models_download_links.json"))[self.file_name]


    def get_stream(self):
        response = requests.get(self.params["link_model"], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.file_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)
