from macro.model_configurations import MODEL_CONFIFURATIONS, TRANSFORMERS_MODELS_FAMILY
from macro.language_dict import SUPPORTED_LANGUAGES



def read_model_inputs(config):
    macro_inputs = {}
    language_label = config.get("language",None)
    macro_inputs["language"] = lang_label_to_iso(language_label)
    
    
    model = config.get("modelName",None)
    model_label =  model["label"]
    model_family = model["value"]

    macro_inputs["model_label"] = model_label
    macro_inputs["model_family"] = model_family
    
    
    is_new_output_folder = config.get("outputFolder",None)
    if is_new_output_folder["value"] == "create_new_folder":
        macro_inputs["is_new_output_folder"] = True
        macro_inputs["new_output_folder_name"] = config.get("newOutputFolder",None)
    else:
        macro_inputs["is_new_output_folder"] = False
        macro_inputs["output_folder_id"] = is_new_output_folder["value"]

    macro_inputs["transformer_shortcut_name"] = config.get("transformersModelVersion",None)

    model_ids = MODEL_CONFIFURATIONS.keys()
    if model_family in model_ids:
        macro_inputs["model_id"] = model_family
    else:
         macro_inputs["model_id"] = macro_inputs["transformer_shortcut_name"]

    return macro_inputs

def is_folder_exist(project,output_folder_name):
    managed_folders_list = [x["name"] for x in project.list_managed_folders()]
    return True if output_folder_name in managed_folders_list else False

def manage_model_folder(output_folder_name,project_key,client):
    project = client.get_project(project_key)

    #If needed, create the managed folder
    if not is_folder_exist(project,output_folder_name):
        output_folder = project.create_managed_folder(output_folder_name)
    
    return output_folder


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

def check_macro_inputs(config):
    language = config.get("language",None)
    modelName = config.get("modelName",None)
    outputFolder = config.get("outputFolder",None)
    newOutputFolder = config.get("newOutputFolder",None)
    transformersModelVersion = config.get("transformersModelVersion",None)

    assert (language is not None), "Language field is missing"
    assert (modelName is not None), "Model field is missing"
    assert (outputFolder is not None), "Output Folder field is missing"
    
    if outputFolder["value"] == "create_new_folder":
        assert (newOutputFolder is not None), "New Output Folder Name field is missing"

    if  modelName["value"] in TRANSFORMERS_MODELS_FAMILY:
        assert (transformersModelVersion is not None), "Model version field is missing"
    
