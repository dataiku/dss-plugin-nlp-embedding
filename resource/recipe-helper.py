import dataiku
from macro.model_configurations import MODEL_CONFIFURATIONS
from macro.language_dict import SUPPORTED_LANGUAGES

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
    languages = list(set([item for sublist in languages for item in sublist]))
    languages_labels = lang_iso_to_label(languages)
    return {'languages': languages_labels}


def get_models(config):
    language_label = config.get("language")
    language = lang_label_to_iso(language_label)
    models = []
    models = [m["family"] for m in MODEL_CONFIFURATIONS.values() if language in m["language_list"]]
    return {'models': models}

def get_transformer_model_versions(config):
    model = config.get("modelName")
    transformer_model_versions = [x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model]
    return {"transformer_model_versions": transformer_model_versions,
            "model_name" : model}

def lang_iso_to_label(languages_iso):
    languages_labels = []
    for language in languages_iso:
        search = [x for x in SUPPORTED_LANGUAGES if x["value"] == language]
        if search:
            languages_labels.append(search[0]["label"])
        else:
            languages_labels.append(language)
    return languages_labels

def lang_label_to_iso(language_label):
    search = [x for x in SUPPORTED_LANGUAGES if x["label"] == language_label]
    if search:
        return search[0]["value"]
    else:
        return language_label
