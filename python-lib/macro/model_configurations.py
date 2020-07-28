MODEL_CONFIFURATIONS = {
    "word2vec": {
        "id": "word2vec",
        "family": "Word2Vec",
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
        "id": "fasttext",
        "family": "FastText",
        "language_list": ["en", "ar"],
        "download_info": {
            "en": "en",
            "ar": "ar"
        }
    },

    "glove": {
        "id": "glove",
        "family": "Glove",
        "language_list": ["en"],
        "download_info": {
            "en": "http://nlp.stanford.edu/data/glove.42B.300d.zip"
        }
    },

    "elmo": {
        "id": "elmo",
        "family": "ELMo",
        "language_list": ["en"],
        "download_info": {
            "en": "https://tfhub.dev/google/elmo/3?tf-hub-format=compressed"
        }
    },

    "use": {
        "id": "use",
        "family": "USE",
        "language_list": ["en", "multilingual"],
        "download_info": {
            "en": "https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed",
            "multilingual": "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3?tf-hub-format=compressed"
        }
    },


    "bert-base-multilingual-cased": {
        "id": "bert-base-multilingual-cased",
        "family": "Bert",
        "language_list": ["multilingual"],
        "download_info": {
            "multilingual": "bert-base-multilingual-cased"
        }
    },

    "distilbert-base-uncased": {
        "id": "distilbert-base-uncased",
        "family": "DistilBert",
        "language_list": ["en"],
        "download_info": {
            "multilingual": "distilbert-base-uncased"
        }
    }
}

TRANSFORMERS_LIST = ["bert-base-multilingual-cased","distilbert-base-uncased"]

