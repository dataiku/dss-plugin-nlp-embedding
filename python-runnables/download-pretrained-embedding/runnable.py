# -*- coding: utf-8 -*-

import dataiku
from dataiku.runnables import Runnable
from macro_utils import (word2vec_downloader,
                         fasttext_downloader,
                         elmo_downloader
                         )

import zipfile
import json
import os

MODELS_DOWNLOAD_LINKS = {
    
    "word2vec-english": {
        "model": "word2vec",  
        "language" : "english",
        "params": {
            "link_model" : "https://docs.google.com/uc?export=download",
            "id_model" : "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
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


class MyRunnable(Runnable):
    """The base interface for a Python runnable"""

    def __init__(self, project_key, config, plugin_config):
        """
        :param project_key: the project in which the runnable executes
        :param config: the dict of the configuration of the object
        :param plugin_config: contains the plugin settings
        """
        self.project_key = project_key
        self.config = config
        self.plugin_config = plugin_config
        self.client = dataiku.api_client()
        self.params = MODELS_DOWNLOAD_LINKS

    def get_progress_target(self):
        """
        If the runnable will return some progress info, have this function return a tuple of
        (target, unit) where unit is one of: SIZE, FILES, RECORDS, NONE
        """
        return (100, 'NONE')

    def run(self, progress_callback):

        # Retrieving parameters
        output_folder_name = self.config.get('outputName', '')
        source = self.config.get('source', '')
        if source == 'fasttext':
            text_language = self.config.get('text_language_fasttext', '')
        else:
            text_language = self.config.get('text_language_other', '')

        # Creating new Managed Folder if needed
        project = self.client.get_project(self.project_key)
        output_folder_found = False

        for folder in project.list_managed_folders():
            if output_folder_name == folder['name']:
                output_folder = project.get_managed_folder(folder['id'])
                output_folder_found = True
                break

        if not output_folder_found:
            output_folder = project.create_managed_folder(output_folder_name)

        output_folder = dataiku.Folder(output_folder.get_definition()["id"],
                                       project_key=self.project_key)

        #######################################
        # Downloading and extracting the data
        #######################################

        if source == 'word2vec':
            word2vec_downloader(output_folder,text_language).download()


        elif source == 'fasttext':
            fasttext_downloader(output_folder,text_language,self.params).download()


        elif source == 'glove':
            if text_language == 'english':
                url = 'http://nlp.stanford.edu/data/glove.42B.300d.zip'
            else:
                raise NotImplementedError("GloVe vectors are only available for English. Use fastText for other languages.")

            archive_name = os.path.basename(url)

            # Download archive
            r = requests.get(url, stream=True)
            with output_folder.get_writer(archive_name) as w:
                for chunk in r.iter_content(chunk_size=100000):
                    if chunk:
                        w.write(chunk)

            file_basename = os.path.splitext(archive_name)[0]
            file_name = file_basename + '.txt'
            file_rename = "GloVe_embeddings"

            # Unzip archive into same directory
            zip_ref = zipfile.ZipFile(os.path.join(
                output_folder_path, archive_name), 'r')
            zip_ref.extractall(output_folder_path)
            zip_ref.close()

            # remove archive
            os.remove(os.path.join(output_folder_path, archive_name))
            # rename embedding file
            os.rename(os.path.join(output_folder_path, file_name), os.path.join(output_folder_path, file_rename))


        elif source == 'elmo':
            elmo_downloader(output_folder,text_language,self.params).download()
            
        else:
            raise NotImplementedError(
                "Only Word2vec, GloVe and FastText embeddings are supported.")
        return "<br><span>The model was downloaded successfuly !</span>"
