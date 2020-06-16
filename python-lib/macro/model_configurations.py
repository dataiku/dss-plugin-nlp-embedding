MODEL_CONFIFURATIONS = {
    "Word2vec": {
        "English": {
            "model_link" : "https://docs.google.com/uc?export=download",
            "id_gdrive": "0B7XkCwpI5KDYNlNUTTlSS21pQmM"
        },
        "Dutch": {
            "model_id" : 39 
        }
    },

    "FastText": {
        "English":  "en",
        "Arabic": "ar"
    },

    "Glove": {
        "English": {
            "model_link": "http://nlp.stanford.edu/data/glove.42B.300d.zip"
        }
    },

    "ELMo": {
        "English": {
            "model_link": "https://tfhub.dev/google/elmo/3?tf-hub-format=compressed"
        }
    },

    "Universal Sentence Encoder": {
        "English": {
            "model_link": "https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed"
        },
        "Multilingual": {
            "model_link": "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"
        }
    },

    "Transformers": {
        "BERT": {
            "English": [
                "bert-base-uncased",
                "bert-large-uncased",
                "bert-base-cased",
                "bert-large-cased",
                "bert-large-uncased-whole-word-masking",
                "bert-large-cased-whole-word-masking"
            ],

            "Multilingual": [
                "bert-base-multilingual-uncased",
                "bert-base-multilingual-cased",

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
        },

        "DistilBERT": {
            "English": [
                "distilbert-base-uncased",
                "distilbert-base-uncased-distilled-squad",
                "distilbert-base-cased"
            ],

            "German": [
                "distilbert-base-german-cased"
            ]
        },

        "GPT-2": {
            "English": [
                "gpt2",
                "gpt2-medium",
                "gpt2-large",
                "gpt2-xl"
            ]
        }
    }


}
