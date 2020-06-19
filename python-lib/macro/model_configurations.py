MODEL_CONFIFURATIONS = {
    
    "word2vec": {
        "label": "Word2vec",
        "languages": {
            "english": {
                "model_link" : "https://docs.google.com/uc?export=download",
                "id_gdrive": "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
            },
            "dutch": {
                "model_id" : 39 
            }
        }
    },

    "fasttext": {
        "label": "FastText",
        "languages": {
            "english":  "en",
            "arabic": "ar"
        }        
    },

    "glove": {
        "label": "Glove",
        "languages": {
            "english": {
                "model_link": "http://nlp.stanford.edu/data/glove.42B.300d.zip"
            }
        }
        
    },

    "elmo": {
        "label": "ELMo",
        "languages": {
            "english": {
                "model_link": "https://tfhub.dev/google/elmo/3?tf-hub-format=compressed"
            }
        }
       
    },

    "use": {
        "label": "Universal Sentence Encoder",
        "languages": {
            "multilingual": {
                "model_link": "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3?tf-hub-format=compressed"
            },
            "english": {
                "model_link": "https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed"
            }
        }
    },

    "transformers": {
        "label": "Transformers",
        "architectures": {
            "bert": {
                "label": "BERT",
                "languages": {
                    "multilingual": [
                    "bert-base-multilingual-uncased",
                    "bert-base-multilingual-cased"

                    ],
                    "english": [
                        "bert-base-uncased",
                        "bert-large-uncased",
                        "bert-base-cased",
                        "bert-large-cased",
                        "bert-large-uncased-whole-word-masking",
                        "bert-large-cased-whole-word-masking"
                    ],

                    "Chinese": [
                        "bert-base-chinese"
                    ],

                    "German": [
                        "bert-base-german-cased"
                    ],

                    "Japanese": [
                        "cl-tohoku/bert-base-japanese"
                    ]
                }
                
            },

            "distilbert": {
                "label": "DistilBERT",
                "languages": {
                    "English": [
                        "distilbert-base-uncased",
                        "distilbert-base-uncased-distilled-squad",
                        "distilbert-base-cased"
                    ],

                    "German": [
                        "distilbert-base-german-cased"
                    ]
                }
                
            },

            "gpt2": {
                "label": "GPT-2",
                "languages": {
                    "English": [
                        "gpt2",
                        "gpt2-medium",
                        "gpt2-large",
                        "gpt2-xl"
                    ]
                }
                
            }
        }   
    }


}


TRANSFORMERS_CONF = {
    "bert-base-multilingual-cased": {
        "label": "bert-base-multilingual-cased",
        "family": "Bert",
        "language_list": ["multilingual"],
        "download_info": {
            "multilingual": "bert-base-multilingual-cased"
        }
    },

    "distilbert-base-uncased": {
        "label": "distilbert-base-uncased",
        "family": "DistilBert",
        "language_list": ["en"],
        "download_info": {
            "multilingual": "distilbert-base-uncased"
        }
    }

}

MODELS_CONF = {
    "word2vec": {
        "label": "Word2Vec",
        "language_list": ["en","du"],
        "download_info": {
            "en": {
                "model_link": "https://docs.google.com/uc?export=download",
                "id_gdrive": "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
            },
            "du": {
                "model_id" : 39
            }
        }
    },

    "fasttext": {
        "label": "FastText",
        "language_list": ["en", "ar"],
        "download_info": {
            "en": "en",
            "ar": "ar"
        }
    }
}



