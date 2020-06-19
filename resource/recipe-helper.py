import dataiku
from macro.model_configurations import (MODELS_CONF,
                                        TRANSFORMERS_CONF)

def do(payload, config, plugin_config, inputs):
    if payload["method"] == "get_languages":
        return get_languages()
    
    if payload["method"] == "get_models":
        return get_models(config)
        
    if payload["method"] == "get_architectures":
        return get_architectures(config)


def get_languages():
    #MODEL_CONFS
    languages = [m["language_list"] for m in MODELS_CONF.values()]
    return {'languages': languages}