from macro.model_configurations import MODEL_CONFIFURATIONS
from macro.language_dict import SUPPORTED_LANGUAGES



def read_model_inputs(config):
    macro_inputs = {}
    language_label = config.get("language",None)
    macro_inputs["language"] = 
    #Add mapping language ISO <--> Language readable format
    
    model_name = config.get("modelName",None)
    model_id =[x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model_name][0] 
    macro_inputs["embedding_model"] = model_id
    macro_inputs["embedding_family"] = model_name

    macro_inputs["output_folder_name"] = config.get("outputFolder",None)
    macro_inputs["transformer_shortcut_name"] = config.get("transformersModelVersion",None)

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