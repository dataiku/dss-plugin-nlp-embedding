def read_model_inputs(config):
    macro_inputs = {}

    
    #Output Folder
    macro_inputs["output_folder_name"] = config.get('outputName', '')

    #Embedding model
    macro_inputs["embedding_model"] = config.get('embedding_model', '')

    #Language
    if macro_inputs["embedding_model"] == "word2vec":
        macro_inputs["language"]= config.get('language_word2vec', '')

    elif macro_inputs["embedding_model"] == "fasttext":
        macro_inputs["language"]= config.get('language_fasttext', '')

    elif macro_inputs["embedding_model"] == "glove":
        macro_inputs["language"]= config.get('language_glove', '')

    elif macro_inputs["embedding_model"] == "elmo":
        macro_inputs["language"]= config.get('language_elmo', '')

    elif macro_inputs["embedding_model"] == "use":
        macro_inputs["language"]= config.get('language_use', '')

    elif macro_inputs["embedding_model"] == "transformers":
        macro_inputs["transformer_architecture"] = config.get('transformer_architecture', '')

        if macro_inputs["transformer_architecture"] == "bert":
            macro_inputs["language"]= config.get('language_tranformer_bert', '') 
            if macro_inputs["language"]== "multilingual":
                macro_inputs["model_shortcut_name"] = config.get('language_tranformer_bert_multilingual','')
            elif macro_inputs["language"]== "english":
                macro_inputs["model_shortcut_name"] = config.get('language_tranformer_bert_english','')

        elif macro_inputs["transformer_architecture"] == "distilbert":
            macro_inputs["language"]= config.get('language_tranformer_distilbert', '') 
            if macro_inputs["language"]== "english":
                macro_inputs["model_shortcut_name"] = config.get('language_tranformer_distilbert_english','')
            elif macro_inputs["language"]== "german":
                macro_inputs["model_shortcut_name"] = config.get('language_tranformer_distilbert_german','')

    
    proxy = {}
    advanced_settings = config['advanced_settings']
    if advanced_settings:
        proxy = config['proxy_config']
        if proxy:
            proxy = proxy["custom_proxy_config"]
    macro_inputs["proxy"] = proxy

    return macro_inputs