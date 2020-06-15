# -*- coding: utf-8 -*-

import dataiku
from dataiku.runnables import Runnable
from macro.model_downloaders import (Word2vecDownloader,
                                    FasttextDownloader,
                                    GloveDownloader,
                                    ElmoDownloader,
                                    UseDownloader,
                                    HuggingFaceDownloader
                                    )

import zipfile
import json
import os


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
        proxy = {}
        advanced_settings = self.config['advanced_settings']
        if advanced_settings:
            proxy = self.config['proxy_config']
            if proxy:
                proxy = proxy["custom_proxy_config"]

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
            model_id = source + "-" + text_language
            Word2vecDownloader(output_folder,model_id,proxy).download()


        elif source == 'fasttext':
            model_id = source + "-" + text_language
            FasttextDownloader(output_folder,model_id,proxy).download()


        elif source == 'glove':
            model_id = source + "-" + text_language
            GloveDownloader(output_folder,model_id,proxy).download()

        elif source == 'elmo':
            model_id = source + "-" + text_language
            ElmoDownloader(output_folder,model_id,proxy).download()

        elif source == 'use':
            model_id = source + "-" + text_language
            UseDownloader(output_folder,model_id,proxy).download() 

        elif source == 'bert-base-uncased':
            model_id = source
            HuggingFaceDownloader(output_folder,model_id,proxy).download() 
        
        return "<br><span>The model was downloaded successfuly !</span>"
