from macro.model_configurations import MODEL_CONFIFURATIONS


def do(payload, config, plugin_config, inputs):
    print("payload: {}".format(payload))
    print("config: {}".format(config))
    print("plugin_config: {}".format(plugin_config))
    print("inputs: {}".format(inputs))
    parameter_name =  payload["parameterName"]
    if parameter_name == "embedding_model":
        values = MODEL_CONFIFURATIONS.keys()
        labels = [x.lower().replace(" ","_") for x in MODEL_CONFIFURATIONS.keys()]
        choices = [{"value": v, "label": l} for v,l in zip(labels,values)]

    elif parameter_name == "language":
        model = config["embedding_model"]
        values = MODEL_CONFIFURATIONS[model]
    
    
    print(stop)
    
    return {"choices": choices}
