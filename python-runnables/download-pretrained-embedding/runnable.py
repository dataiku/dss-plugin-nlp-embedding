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
from macro.macro_utils import read_model_inputs, check_macro_inputs
from macro.model_configurations import TRANSFORMERS_MODELS
import zipfile
import json
import os
import logging

FORMAT = '[Embedding Downloader] %(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()


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

        # Check marco inputs
        check_macro_inputs(self.config)

        # Retrieving parameters
        macro_inputs = read_model_inputs(self.config)

        # Creating new Managed Folder if needed
        if macro_inputs["is_new_output_folder"]:
            logger.info("Creating new managed folder...")
            new_output_folder_name = macro_inputs["new_output_folder_name"]
            project = self.client.get_project(self.project_key)
            managed_folders = project.list_managed_folders()
            managed_folders_names = [x["name"] for x in managed_folders]
            assert (new_output_folder_name not in managed_folders_names), "Managed folder {} already exists.".format(new_output_folder_name)
            output_folder = project.create_managed_folder(new_output_folder_name)        
            output_folder = dataiku.Folder(output_folder.get_definition()["id"],
                                project_key=self.project_key)

        else:
            output_folder = dataiku.Folder(macro_inputs["output_folder_id"],
                                       project_key=self.project_key)


        #######################################
        # Downloading and extracting the data
        #######################################

        embedding_model = macro_inputs["embedding_model"]
        proxy = self.plugin_config["proxy"]
        if embedding_model == 'word2vec':
            Word2vecDownloader(output_folder,macro_inputs,proxy,progress_callback).run()

        elif embedding_model == 'fasttext':
            FasttextDownloader(output_folder,macro_inputs,proxy,progress_callback).run()

        elif embedding_model == 'glove':
            GloveDownloader(output_folder,macro_inputs,proxy,progress_callback).run()

        elif embedding_model == 'elmo':
            ElmoDownloader(output_folder,macro_inputs,proxy,progress_callback).run()

        elif embedding_model == 'use':
            UseDownloader(output_folder,macro_inputs,proxy,progress_callback).run() 

        elif embedding_model in TRANSFORMERS_MODELS:
            HuggingFaceDownloader(output_folder,macro_inputs,proxy,progress_callback).run() 
        else:
            raise ValueError("Model not found.")

        return "<br><span>The model was downloaded successfuly !</span>"
