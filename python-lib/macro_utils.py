import json
import requests
import shutil
import gzip
import os

MODELS_DOWNLOAD_LINKS = {
    
    "word2vec-english": {
        "model": "word2vec",  
        "language" : "english",
        "params": {
            "link_model" : "https://docs.google.com/uc?export=download",
            "id_gdrive" : "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
        }
    },

    "fasttext-english" : {
        "model" : "fasttext",    
        "language" : "english",
        "params": {
            "link_model" : "https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.en.vec"
        }
    },

    "fasttext-french" : {
        "model" : "fasttext",    
        "language" : "french",
        "params": {
            "link_model" : "https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.fr.vec"
        }
    },

    "fasttext-german" : {
        "model" : "fasttext",    
        "language" : "german",
        "params": {
            "link_model" : "https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.de.vec"
        }
    },

    "glove-english" : {
        "model" : "glove",    
        "language" : "english",
        "params": {
            "link_model" : "http://nlp.stanford.edu/data/glove.42B.300d.zip"
        }
    },

    "elmo-english" : {
        "model" : "elmo",    
        "language" : "english",
        "params": {
            "link_model" : "https://tfhub.dev/google/elmo/3?tf-hub-format=compressed"
        }
    },

    "use-english" : {
        "model" : "use",    
        "language" : "english",
        "params": {
            "link_model" : "https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed"
        }
    },

    "bert-base-uncased" : {
        "model" : "bert",    
        "language" : "english",
        "params": {
            "link_model" : "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-pytorch_model.bin",
            "link_config" : "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-config.json",
            "link_vocab" : "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt"
        }
    }
}



class BaseDownloader(object):
    def __init__(self,folder,model_id):
        self.folder = folder
        self.model_id = model_id
        self.model_params = MODELS_DOWNLOAD_LINKS[self.model_id]
        self.archive_name = self.model_id



    def get_stream(self,parameter = "link_model"):
        response = requests.get(self.model_params["params"][parameter], stream=True)
        return response

    def download(self):
        response = self.get_stream()
        with self.folder.get_writer(self.archive_name) as w:
            for chunk in response.iter_content(chunk_size=100000):
                if chunk:
                    w.write(chunk)

class Word2vecDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)
        self.archive_name = self.model_id + ".bin.gz"


    def get_stream(self,link = "link_model"):
        session = requests.Session()
        response = session.get(self.model_params["params"]["link_model"], params={'id': self.model_params["params"]["id_gdrive"]}, stream=True)
        token = self.__get_confirm_token(response)

        if token:
            params = {'id': self.model_params["params"]["id_gdrive"], 'confirm': token}
            response = session.get(self.model_params["params"]["link_model"], params=params, stream=True)
        else:
            raise RuntimeError("Google Drive Token could not be verified.")

        return response

    def download(self):
        response = self.get_stream()
        destination_writer = self.folder.get_writer(self.archive_name)

        #Write .gz file to folder
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:  # filter out keep-alive new chunks
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


class FasttextDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)


class GloveDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)
        self.archive_name = self.model_id + ".zip"


class ElmoDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)

class UseDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)

class HuggingFaceDownloader(BaseDownloader):
    def __init__(self,folder,model_id):
        BaseDownloader.__init__(self,folder,model_id)

    def download(self):
        for parameter, file_link in self.model_params["params"].items():
            response = self.get_stream(parameter)
            with self.folder.get_writer(file_name) as w:
                for chunk in response.iter_content(chunk_size=100000):
                    if chunk:
                        w.write(chunk)