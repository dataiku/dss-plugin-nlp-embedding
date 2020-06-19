MODEL_CONFIFURATIONS = {
    "word2vec": {
        "id": "word2vec",
        "label": "Word2Vec",
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
        "label": "FastText",
        "family": "FastText",
        "language_list": ["en", "ar"],
        "download_info": {
            "en": "en",
            "ar": "ar"
        }
    },

    "bert-base-multilingual-cased": {
        "id": "bert-base-multilingual-cased",
        "label": "bert-base-multilingual-cased",
        "family": "Bert",
        "language_list": ["multilingual"],
        "download_info": {
            "multilingual": "bert-base-multilingual-cased"
        }
    },

    "distilbert-base-uncased": {
        "id": "distilbert-base-uncased",
        "label": "distilbert-base-uncased",
        "family": "DistilBert",
        "language_list": ["en"],
        "download_info": {
            "multilingual": "distilbert-base-uncased"
        }
    }
}

TRANSFORMERS_LIST = ["bert-base-multilingual-cased","distilbert-base-uncased"]

