def read_model_inputs(config):
    macro_inputs = {}

    macro_inputs["output_folder_name"] = config.get("outputFolder",None)
    macro_inputs["language"] = config.get("language",None)
    macro_inputs["modelName"] = config.get("modelName",None)
    
    
    proxy = {}
    macro_inputs["proxy"] = proxy
    '''
    advanced_settings = config['advanced_settings']
    if advanced_settings:
        proxy = config['proxy_config']
        if proxy:
            proxy = proxy["custom_proxy_config"]
    macro_inputs["proxy"] = proxy
    '''

    return macro_inputs