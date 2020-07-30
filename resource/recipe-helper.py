import dataiku
from macro.model_configurations import MODEL_CONFIFURATIONS
from macro.macro_utils import lang_iso_to_label, lang_label_to_iso

def do(payload, config, plugin_config, inputs):
    if payload["method"] == "get_languages":
        return get_languages()
    
    if payload["method"] == "get_models":
        return get_models(config)
        
    if payload["method"] == "get_transformer_model_versions":
        return get_transformer_model_versions(config)

    if payload["method"] == "get_model_description":
        return get_model_description(config)


def get_languages():
    languages= []
    languages = [m["language_list"] for m in MODEL_CONFIFURATIONS.values()]
    languages = list(set([item for sublist in languages for item in sublist]))
    languages_labels = lang_iso_to_label(languages)
    return {'languages': sorted(languages_labels)}


def get_models(config):
    language_label = config.get("language")
    language = lang_label_to_iso(language_label)
    models = [m["family"] for m in MODEL_CONFIFURATIONS.values() if language in m["language_list"]]
    return {'models': list(set(models))}

def get_transformer_model_versions(config):
    model = config.get("modelName")
    language_label = config.get("language")
    language = lang_label_to_iso(language_label)
    transformer_model_versions = [x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model and language in x["language_list"]]
    return {"transformer_model_versions": transformer_model_versions,
            "model_name" : model}

def get_model_description(config):
    model = config.get("transformersModelVersion")
    if model is None:
        model_description = ""
    else:
        model_description = MODEL_CONFIFURATIONS[model]["description"]
    return {'model_description': model_description}


