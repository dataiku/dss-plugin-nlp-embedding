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
    languages= []
    conf_list = [MODELS_CONF,TRANSFORMERS_CONF]
    for conf in conf_list:
        languages.extend([m["language_list"] for m in conf.values()])
    languages = [item for sublist in languages for item in sublist]
    return {'languages': list(set(languages))}


def get_models(config):
    language = config.get("language")
    models = []
    conf_list = [MODELS_CONF,TRANSFORMERS_CONF]
    for conf in conf_list:
        models.extend([m["label"] for m in conf.values() if language in m["language_list"]])
    return {'models': models}

def get_architectures(config):
    return {"architectures": ["foo"]}