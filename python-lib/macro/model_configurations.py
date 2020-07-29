MODEL_CONFIFURATIONS = {
    "word2vec": {
        "id": "word2vec",
        "family": "Word2Vec",
        "language_list": ['en','grc', 'ar', 'eu', 'bg', 'ca', 'zh', 'hr', 'cs', 'da', 'nl', 'et', 'fi', 'fr', 'gl', 'de', 'el', 'he', 'hi', 'hu', 'id', 'ga', 'it', 'ja', 'kk', 'ko', 'la', 'lv', 'nb', 'nn', 'cu', 'fa', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'es', 'sv', 'tr', 'uk', 'ur', 'ug', 'vi'],
        "download_info": {
            "en": {
                "model_link": "https://docs.google.com/uc?export=download",
                "id_gdrive": "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
            },
            'grc': {'model_id': 30},
            'ar': {'model_id': 31},
            'eu': {'model_id': 32},
            'bg': {'model_id': 33},
            'ca': {'model_id': 34},
            'zh': {'model_id': 35},
            'hr': {'model_id': 36},
            'cs': {'model_id': 37},
            'da': {'model_id': 38},
            'nl': {'model_id': 39},
            'et': {'model_id': 41},
            'fi': {'model_id': 42},
            'fr': {'model_id': 43},
            'gl': {'model_id': 44},
            'de': {'model_id': 45},
            'el': {'model_id': 46},
            'he': {'model_id': 47},
            'hi': {'model_id': 48},
            'hu': {'model_id': 49},
            'id': {'model_id': 50},
            'ga': {'model_id': 51},
            'it': {'model_id': 52},
            'ja': {'model_id': 53},
            'kk': {'model_id': 54},
            'ko': {'model_id': 55},
            'la': {'model_id': 56},
            'lv': {'model_id': 57},
            'nb': {'model_id': 58},
            'nn': {'model_id': 59},
            'cu': {'model_id': 60},
            'fa': {'model_id': 61},
            'pl': {'model_id': 62},
            'pt': {'model_id': 63},
            'ro': {'model_id': 64},
            'ru': {'model_id': 65},
            'sk': {'model_id': 66},
            'sl': {'model_id': 67},
            'es': {'model_id': 68},
            'sv': {'model_id': 69},
            'tr': {'model_id': 70},
            'uk': {'model_id': 71},
            'ur': {'model_id': 72},
            'ug': {'model_id': 73},
            'vi': {'model_id': 74}       
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

