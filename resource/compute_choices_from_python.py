from macro.model_configurations import MODEL_CONFIFURATIONS


def do(payload, config, plugin_config, inputs):
    print("payload: {}".format(payload))
    print("config: {}".format(config))
    print("plugin_config: {}".format(plugin_config))
    print("inputs: {}".format(inputs))
    parameter_name =  payload["parameterName"]
    print("parameter_name: {}".format(parameter_name))
    if parameter_name == "embedding_model":
        values = MODEL_CONFIFURATIONS.keys()
        labels = [MODEL_CONFIFURATIONS[x]["label"] for x in values]
        choices = [{"value": v, "label": l} for v,l in zip(values,labels)]

    elif parameter_name == "language":
        if "embedding_model" in config:
            model = config["embedding_model"]
            values = MODEL_CONFIFURATIONS[model]["languages"].keys()
            choices = [{"value": v, "label": l} for v,l in zip(values,values)]
    
    

    
    return {"choices": choices}
