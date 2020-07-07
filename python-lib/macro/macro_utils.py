from macro.model_configurations import MODEL_CONFIFURATIONS

def read_model_inputs(config):
    macro_inputs = {}
    macro_inputs["language"] = config.get("language",None)
    #Add mapping language ISO <--> Language readable format
    
    model_name = config.get("modelName",None)
    model_id =[x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model_name][0] 
    macro_inputs["embedding_model"] = model_id

    macro_inputs["output_folder_name"] = config.get("outputFolder",None)
    macro_inputs["transformer_shortcut_name"] = config.get("transformersModelVersion",None)

    return macro_inputs