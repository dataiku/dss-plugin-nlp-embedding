from macro.model_configurations import MODEL_CONFIFURATIONS


def do(payload, config, plugin_config, inputs):
    values = MODEL_CONFIFURATIONS.keys()
    labels = [x.lower().replace(" ","_") for x in MODEL_CONFIFURATIONS.keys()]
    choices = [{"value": v, "label": l} for v,l in zip(values,labels)}]
    
    return {"choices": choices}
