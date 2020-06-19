import dataiku
from macro.model_configurations import MODEL_CONFIFURATIONS

def do(payload, config, plugin_config, inputs):
    if payload["method"] == "get_languages":
        return get_languages()
    
    if payload["method"] == "get_models":
        return get_models(config)
        
    if payload["method"] == "get_transformer_model_versions":
        return get_transformer_model_versions(config)


def get_languages():
    languages= []
    languages = [m["language_list"] for m in MODEL_CONFIFURATIONS.values()]
    languages = [item for sublist in languages for item in sublist]
    return {'languages': list(set(languages))}


def get_models(config):
    language = config.get("language")
    models = []
    models = [m["family"] for m in MODEL_CONFIFURATIONS.values() if language in m["language_list"]]
    return {'models': models}

def get_transformer_model_versions(config):
    model = config.get("modelName")
    transformer_model_versions = [x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model]
    return {"transformer_model_versions": transformer_model_versions}