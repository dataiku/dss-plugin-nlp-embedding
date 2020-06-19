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
    languages = []
    for conf in [MODELS_CONF,TRANSFORMERS_CONF]
        languages.extend([m["language_list"] for m in conf.values()])
    languages = [item for sublist in languages for item in sublist]
    return {'languages': languages}