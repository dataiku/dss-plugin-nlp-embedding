from transformers import (tokenization_bert,
                          tokenization_gpt2,
                          tokenization_transfo_xl,
                          tokenization_xlnet,
                          tokenization_roberta,
                          tokenization_distilbert,
                          tokenization_ctrl,
                          tokenization_camembert,
                          tokenization_albert,
                          tokenization_t5,
                          tokenization_bart)

NON_TRANSFORMER_MODELS = ["word2vec","fasttext","glove","elmo","use"]
TRANSFORMERS_MODELS = ['bert-base-uncased', 'bert-large-uncased', 'bert-base-cased', 'bert-large-cased', 'bert-base-multilingual-uncased', 'bert-base-multilingual-cased', 'bert-base-chinese', 'bert-base-german-cased', 'bert-large-uncased-whole-word-masking', 'bert-large-cased-whole-word-masking', 'bert-large-uncased-whole-word-masking-finetuned-squad', 'bert-large-cased-whole-word-masking-finetuned-squad', 'bert-base-cased-finetuned-mrpc', 'bert-base-german-dbmdz-cased', 'bert-base-german-dbmdz-uncased', 'cl-tohoku/bert-base-japanese', 'cl-tohoku/bert-base-japanese-whole-word-masking', 'cl-tohoku/bert-base-japanese-char', 'cl-tohoku/bert-base-japanese-char-whole-word-masking', 'TurkuNLP/bert-base-finnish-cased-v1', 'TurkuNLP/bert-base-finnish-uncased-v1', 'wietsedv/bert-base-dutch-cased', 'facebook/bart-large', 'facebook/bart-large-mnli', 'facebook/bart-large-cnn', 'facebook/mbart-large-en-ro', 'openai-gpt', 'transfo-xl-wt103', 'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl', 'distilgpt2', 'ctrl', 'xlnet-base-cased', 'xlnet-large-cased', 'xlm-mlm-en-2048', 'xlm-mlm-ende-1024', 'xlm-mlm-enfr-1024', 'xlm-mlm-enro-1024', 'xlm-mlm-tlm-xnli15-1024', 'xlm-mlm-xnli15-1024', 'xlm-clm-enfr-1024', 'xlm-clm-ende-1024', 'xlm-mlm-17-1280', 'xlm-mlm-100-1280', 'roberta-base', 'roberta-large', 'roberta-large-mnli', 'distilroberta-base', 'roberta-base-openai-detector', 'roberta-large-openai-detector', 'distilbert-base-uncased', 'distilbert-base-uncased-distilled-squad', 'distilbert-base-cased', 'distilbert-base-cased-distilled-squad', 'distilbert-base-german-cased', 'distilbert-base-multilingual-cased', 'albert-base-v1', 'albert-large-v1', 'albert-xlarge-v1', 'albert-xxlarge-v1', 'albert-base-v2', 'albert-large-v2', 'albert-xlarge-v2', 'albert-xxlarge-v2', 'camembert-base', 't5-small', 't5-base', 't5-large', 'xlm-roberta-base', 'xlm-roberta-large', 'flaubert/flaubert_small_cased', 'flaubert/flaubert_base_uncased', 'flaubert/flaubert_base_cased', 'flaubert/flaubert_large_cased', 'allenai/longformer-base-4096', 'allenai/longformer-large-4096']
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
        "language_list": ['af', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'az', 'ba', 'eu', 'be', 'bn', 'bs', 'br', 'bg', 'my', 'ca', 'ce', 'zh', 'cv', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'pa', 'en', 'eo', 'et', 'fi', 'fr', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'he', 'hi', 'hu', 'is', 'io', 'id', 'ia', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'ky', 'ko', 'ku', 'la', 'lv', 'li', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'gv', 'mr', 'mn', 'ne', 'no', 'nn', 'oc', 'or', 'os', 'ps', 'fa', 'pl', 'pt', 'qu', 'ro', 'rm', 'ru', 'sa', 'sc', 'gd', 'sr', 'sh', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'bo', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'vo', 'wa', 'cy', 'fy', 'yi', 'yo'],
        "download_info": {
            'af': 'af',
            'sq': 'sq',
            'am': 'am',
            'ar': 'ar',
            'an': 'an',
            'hy': 'hy',
            'as': 'as',
            'az': 'az',
            'ba': 'ba',
            'eu': 'eu',
            'be': 'be',
            'bn': 'bn',
            'bs': 'bs',
            'br': 'br',
            'bg': 'bg',
            'my': 'my',
            'ca': 'ca',
            'ce': 'ce',
            'zh': 'zh',
            'cv': 'cv',
            'co': 'co',
            'hr': 'hr',
            'cs': 'cs',
            'da': 'da',
            'dv': 'dv',
            'nl': 'nl',
            'pa': 'pa',
            'en': 'en',
            'eo': 'eo',
            'et': 'et',
            'fi': 'fi',
            'fr': 'fr',
            'gl': 'gl',
            'ka': 'ka',
            'de': 'de',
            'el': 'el',
            'gu': 'gu',
            'ht': 'ht',
            'he': 'he',
            'hi': 'hi',
            'hu': 'hu',
            'is': 'is',
            'io': 'io',
            'id': 'id',
            'ia': 'ia',
            'ga': 'ga',
            'it': 'it',
            'ja': 'ja',
            'jv': 'jv',
            'kn': 'kn',
            'kk': 'kk',
            'km': 'km',
            'ky': 'ky',
            'ko': 'ko',
            'ku': 'ku',
            'la': 'la',
            'lv': 'lv',
            'li': 'li',
            'lt': 'lt',
            'lb': 'lb',
            'mk': 'mk',
            'mg': 'mg',
            'ms': 'ms',
            'ml': 'ml',
            'mt': 'mt',
            'gv': 'gv',
            'mr': 'mr',
            'mn': 'mn',
            'ne': 'ne',
            'no': 'no',
            'nn': 'nn',
            'oc': 'oc',
            'or': 'or',
            'os': 'os',
            'ps': 'ps',
            'fa': 'fa',
            'pl': 'pl',
            'pt': 'pt',
            'qu': 'qu',
            'ro': 'ro',
            'rm': 'rm',
            'ru': 'ru',
            'sa': 'sa',
            'sc': 'sc',
            'gd': 'gd',
            'sr': 'sr',
            'sh': 'sh',
            'sd': 'sd',
            'si': 'si',
            'sk': 'sk',
            'sl': 'sl',
            'so': 'so',
            'es': 'es',
            'su': 'su',
            'sw': 'sw',
            'sv': 'sv',
            'tl': 'tl',
            'tg': 'tg',
            'ta': 'ta',
            'tt': 'tt',
            'te': 'te',
            'th': 'th',
            'bo': 'bo',
            'tr': 'tr',
            'tk': 'tk',
            'uk': 'uk',
            'ur': 'ur',
            'ug': 'ug',
            'uz': 'uz',
            'vi': 'vi',
            'vo': 'vo',
            'wa': 'wa',
            'cy': 'cy',
            'fy': 'fy',
            'yi': 'yi',
            'yo': 'yo'           
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
    
    'TurkuNLP/bert-base-finnish-cased-v1': {  'description': '12-layer, '
                                                            '768-hidden, '
                                                            '12-heads, 110M '
                                                            'parameters.\n'
                                                            'Trained on cased '
                                                            'Finnish text.\n'
                                                            '\n'
                                                            '(see details on '
                                                            'turkunlp.org).',
                                             'download_info': {'fi': 'fi'},
                                             'family': 'BERT',
                                             'id': 'TurkuNLP/bert-base-finnish-cased-v1',
                                             'language_list': ['fi']},
   'TurkuNLP/bert-base-finnish-uncased-v1': {  'description': '12-layer, '
                                                              '768-hidden, '
                                                              '12-heads, 110M '
                                                              'parameters.\n'
                                                              'Trained on '
                                                              'uncased Finnish '
                                                              'text.\n'
                                                              '\n'
                                                              '(see details on '
                                                              'turkunlp.org).',
                                               'download_info': {'fi': 'fi'},
                                               'family': 'BERT',
                                               'id': 'TurkuNLP/bert-base-finnish-uncased-v1',
                                               'language_list': ['fi']},
   'albert-base-v1': {  'description': '12 repeating layers, 128 embedding, '
                                       '768-hidden, 12-heads, 11M parameters\n'
                                       'ALBERT base model\n'
                                       '\n',
                        'download_info': {'en': 'en'},
                        'family': 'ALBERT',
                        'id': 'albert-base-v1',
                        'language_list': ['en']},
   'albert-base-v2': {  'description': '12 repeating layers, 128 embedding, '
                                       '768-hidden, 12-heads, 11M parameters\n'
                                       'ALBERT base model with no dropout, '
                                       'additional training data and longer '
                                       'training\n'
                                       '\n',
                        'download_info': {'en': 'en'},
                        'family': 'ALBERT',
                        'id': 'albert-base-v2',
                        'language_list': ['en']},
   'albert-large-v1': {  'description': '24 repeating layers, 128 embedding, '
                                        '1024-hidden, 16-heads, 17M '
                                        'parameters\n'
                                        'ALBERT large model\n'
                                        '\n',
                         'download_info': {'en': 'en'},
                         'family': 'ALBERT',
                         'id': 'albert-large-v1',
                         'language_list': ['en']},
   'albert-large-v2': {  'description': '24 repeating layers, 128 embedding, '
                                        '1024-hidden, 16-heads, 17M '
                                        'parameters\n'
                                        'ALBERT large model with no dropout, '
                                        'additional training data and longer '
                                        'training\n'
                                        '\n',
                         'download_info': {'en': 'en'},
                         'family': 'ALBERT',
                         'id': 'albert-large-v2',
                         'language_list': ['en']},
   'albert-xlarge-v1': {  'description': '24 repeating layers, 128 embedding, '
                                         '2048-hidden, 16-heads, 58M '
                                         'parameters\n'
                                         'ALBERT xlarge model\n'
                                         '\n',
                          'download_info': {'en': 'en'},
                          'family': 'ALBERT',
                          'id': 'albert-xlarge-v1',
                          'language_list': ['en']},
   'albert-xlarge-v2': {  'description': '24 repeating layers, 128 embedding, '
                                         '2048-hidden, 16-heads, 58M '
                                         'parameters\n'
                                         'ALBERT xlarge model with no dropout, '
                                         'additional training data and longer '
                                         'training\n'
                                         '\n',
                          'download_info': {'en': 'en'},
                          'family': 'ALBERT',
                          'id': 'albert-xlarge-v2',
                          'language_list': ['en']},
   'albert-xxlarge-v1': {  'description': '12 repeating layer, 128 embedding, '
                                          '4096-hidden, 64-heads, 223M '
                                          'parameters\n'
                                          'ALBERT xxlarge model\n'
                                          '\n',
                           'download_info': {'en': 'en'},
                           'family': 'ALBERT',
                           'id': 'albert-xxlarge-v1',
                           'language_list': ['en']},
   'albert-xxlarge-v2': {  'description': '12 repeating layer, 128 embedding, '
                                          '4096-hidden, 64-heads, 223M '
                                          'parameters\n'
                                          'ALBERT xxlarge model with no '
                                          'dropout, additional training data '
                                          'and longer training\n'
                                          '\n',
                           'download_info': {'en': 'en'},
                           'family': 'ALBERT',
                           'id': 'albert-xxlarge-v2',
                           'language_list': ['en']},
   'allenai/longformer-base-4096': {  'description': '12-layer, 768-hidden, '
                                                     '12-heads, ~149M '
                                                     'parameters\n'
                                                     'Starting from '
                                                     'RoBERTa-base checkpoint, '
                                                     'trained on documents of '
                                                     'max length 4,096',
                                      'download_info': {'en': 'en'},
                                      'family': 'Longformer',
                                      'id': 'allenai/longformer-base-4096',
                                      'language_list': ['en']},
   'allenai/longformer-large-4096': {  'description': '24-layer, 1024-hidden, '
                                                      '16-heads, ~435M '
                                                      'parameters\n'
                                                      'Starting from '
                                                      'RoBERTa-large '
                                                      'checkpoint, trained on '
                                                      'documents of max length '
                                                      '4,096',
                                       'download_info': {'en': 'en'},
                                       'family': 'Longformer',
                                       'id': 'allenai/longformer-large-4096',
                                       'language_list': ['en']},
   'bert-base-cased': {  'description': '12-layer, 768-hidden, 12-heads, 110M '
                                        'parameters.\n'
                                        'Trained on cased English text.',
                         'download_info': {'en': 'en'},
                         'family': 'BERT',
                         'id': 'bert-base-cased',
                         'language_list': ['en']},
   'bert-base-cased-finetuned-mrpc': {  'description': '12-layer, 768-hidden, '
                                                       '12-heads, 110M '
                                                       'parameters.\n'
                                                       'The bert-base-cased '
                                                       'model fine-tuned on '
                                                       'MRPC\n'
                                                       '\n'
                                                       '(see details of '
                                                       'fine-tuning in the '
                                                       'example section)',
                                        'download_info': {'en': 'en'},
                                        'family': 'BERT',
                                        'id': 'bert-base-cased-finetuned-mrpc',
                                        'language_list': ['en']},
   'bert-base-chinese': {  'description': '12-layer, 768-hidden, 12-heads, '
                                          '110M parameters.\n'
                                          'Trained on cased Chinese Simplified '
                                          'and Traditional text.',
                           'download_info': {'zh': 'zh'},
                           'family': 'BERT',
                           'id': 'bert-base-chinese',
                           'language_list': ['zh']},
   'bert-base-german-cased': {  'description': '12-layer, 768-hidden, '
                                               '12-heads, 110M parameters.\n'
                                               'Trained on cased German text '
                                               'by Deepset.ai\n'
                                               '\n'
                                               '(see details on deepset.ai '
                                               'website).',
                                'download_info': {'de': 'de'},
                                'family': 'BERT',
                                'id': 'bert-base-german-cased',
                                'language_list': ['de']},
   'bert-base-german-dbmdz-cased': {  'description': '12-layer, 768-hidden, '
                                                     '12-heads, 110M '
                                                     'parameters.\n'
                                                     'Trained on cased German '
                                                     'text by DBMDZ\n'
                                                     '\n'
                                                     '(see details on dbmdz '
                                                     'repository).',
                                      'download_info': {'de': 'de'},
                                      'family': 'BERT',
                                      'id': 'bert-base-german-dbmdz-cased',
                                      'language_list': ['de']},
   'bert-base-german-dbmdz-uncased': {  'description': '12-layer, 768-hidden, '
                                                       '12-heads, 110M '
                                                       'parameters.\n'
                                                       'Trained on uncased '
                                                       'German text by DBMDZ\n'
                                                       '\n'
                                                       '(see details on dbmdz '
                                                       'repository).',
                                        'download_info': {'de': 'de'},
                                        'family': 'BERT',
                                        'id': 'bert-base-german-dbmdz-uncased',
                                        'language_list': ['de']},
   'bert-base-multilingual-cased': {  'description': '(New, recommended) '
                                                     '12-layer, 768-hidden, '
                                                     '12-heads, 110M '
                                                     'parameters.\n'
                                                     'Trained on cased text in '
                                                     'the top 104 languages '
                                                     'with the largest '
                                                     'Wikipedias\n'
                                                     '\n'
                                                     '.',
                                      'download_info': {  'multilingual': 'multilingual'},
                                      'family': 'BERT',
                                      'id': 'bert-base-multilingual-cased',
                                      'language_list': ['multilingual']},
   'bert-base-multilingual-uncased': {  'description': '(Original, not '
                                                       'recommended) 12-layer, '
                                                       '768-hidden, 12-heads, '
                                                       '110M parameters.\n'
                                                       'Trained on lower-cased '
                                                       'text in the top 102 '
                                                       'languages with the '
                                                       'largest Wikipedias\n'
                                                       '\n'
                                                       '.',
                                        'download_info': {  'multilingual': 'multilingual'},
                                        'family': 'BERT',
                                        'id': 'bert-base-multilingual-uncased',
                                        'language_list': ['multilingual']},
   'bert-base-uncased': {  'description': '12-layer, 768-hidden, 12-heads, '
                                          '110M parameters.\n'
                                          'Trained on lower-cased English '
                                          'text.',
                           'download_info': {'en': 'en'},
                           'family': 'BERT',
                           'id': 'bert-base-uncased',
                           'language_list': ['en']},
   'bert-large-cased': {  'description': '24-layer, 1024-hidden, 16-heads, '
                                         '340M parameters.\n'
                                         'Trained on cased English text.',
                          'download_info': {'en': 'en'},
                          'family': 'BERT',
                          'id': 'bert-large-cased',
                          'language_list': ['en']},
   'bert-large-cased-whole-word-masking': {  'description': '24-layer, '
                                                            '1024-hidden, '
                                                            '16-heads, 340M '
                                                            'parameters.\n'
                                                            'Trained on cased '
                                                            'English text '
                                                            'using '
                                                            'Whole-Word-Masking\n'
                                                            '\n'
                                                            '.',
                                             'download_info': {'en': 'en'},
                                             'family': 'BERT',
                                             'id': 'bert-large-cased-whole-word-masking',
                                             'language_list': ['en']},
   'bert-large-cased-whole-word-masking-finetuned-squad': {  'description': '24-layer, '
                                                                            '1024-hidden, '
                                                                            '16-heads, '
                                                                            '340M '
                                                                            'parameters\n'
                                                                            'The '
                                                                            'bert-large-cased-whole-word-masking '
                                                                            'model '
                                                                            'fine-tuned '
                                                                            'on '
                                                                            'SQuAD\n'
                                                                            '\n'
                                                                            '(see '
                                                                            'details '
                                                                            'of '
                                                                            'fine-tuning '
                                                                            'in '
                                                                            'the '
                                                                            'example '
                                                                            'section)',
                                                             'download_info': {  'en': 'en'},
                                                             'family': 'BERT',
                                                             'id': 'bert-large-cased-whole-word-masking-finetuned-squad',
                                                             'language_list': [  'en']},
   'bert-large-uncased': {  'description': '24-layer, 1024-hidden, 16-heads, '
                                           '340M parameters.\n'
                                           'Trained on lower-cased English '
                                           'text.',
                            'download_info': {'en': 'en'},
                            'family': 'BERT',
                            'id': 'bert-large-uncased',
                            'language_list': ['en']},
   'bert-large-uncased-whole-word-masking': {  'description': '24-layer, '
                                                              '1024-hidden, '
                                                              '16-heads, 340M '
                                                              'parameters.\n'
                                                              'Trained on '
                                                              'lower-cased '
                                                              'English text '
                                                              'using '
                                                              'Whole-Word-Masking\n'
                                                              '\n'
                                                              '.',
                                               'download_info': {'en': 'en'},
                                               'family': 'BERT',
                                               'id': 'bert-large-uncased-whole-word-masking',
                                               'language_list': ['en']},
   'bert-large-uncased-whole-word-masking-finetuned-squad': {  'description': '24-layer, '
                                                                              '1024-hidden, '
                                                                              '16-heads, '
                                                                              '340M '
                                                                              'parameters.\n'
                                                                              'The '
                                                                              'bert-large-uncased-whole-word-masking '
                                                                              'model '
                                                                              'fine-tuned '
                                                                              'on '
                                                                              'SQuAD\n'
                                                                              '\n'
                                                                              '(see '
                                                                              'details '
                                                                              'of '
                                                                              'fine-tuning '
                                                                              'in '
                                                                              'the '
                                                                              'example '
                                                                              'section).',
                                                               'download_info': {  'en': 'en'},
                                                               'family': 'BERT',
                                                               'id': 'bert-large-uncased-whole-word-masking-finetuned-squad',
                                                               'language_list': [  'en']},
   'camembert-base': {  'description': '12-layer, 768-hidden, 12-heads, 110M '
                                       'parameters\n'
                                       'CamemBERT using the BERT-base '
                                       'architecture\n'
                                       '\n',
                        'download_info': {'fr': 'fr'},
                        'family': 'CamemBERT',
                        'id': 'camembert-base',
                        'language_list': ['fr']},
   'cl-tohoku/bert-base-japanese': {  'description': '12-layer, 768-hidden, '
                                                     '12-heads, 110M '
                                                     'parameters.\n'
                                                     'Trained on Japanese '
                                                     'text. Text is tokenized '
                                                     'with MeCab and '
                                                     'WordPiece.\n'
                                                     'MeCab is required for '
                                                     'tokenization.\n'
                                                     '\n'
                                                     '(see details on '
                                                     'cl-tohoku repository).',
                                      'download_info': {'ja': 'ja'},
                                      'family': 'BERT',
                                      'id': 'cl-tohoku/bert-base-japanese',
                                      'language_list': ['ja']},
   'cl-tohoku/bert-base-japanese-char': {  'description': '12-layer, '
                                                          '768-hidden, '
                                                          '12-heads, 110M '
                                                          'parameters.\n'
                                                          'Trained on Japanese '
                                                          'text. Text is '
                                                          'tokenized into '
                                                          'characters.\n'
                                                          '\n'
                                                          '(see details on '
                                                          'cl-tohoku '
                                                          'repository).',
                                           'download_info': {'ja': 'ja'},
                                           'family': 'BERT',
                                           'id': 'cl-tohoku/bert-base-japanese-char',
                                           'language_list': ['ja']},
   'cl-tohoku/bert-base-japanese-char-whole-word-masking': {  'description': '12-layer, '
                                                                             '768-hidden, '
                                                                             '12-heads, '
                                                                             '110M '
                                                                             'parameters.\n'
                                                                             'Trained '
                                                                             'on '
                                                                             'Japanese '
                                                                             'text '
                                                                             'using '
                                                                             'Whole-Word-Masking. '
                                                                             'Text '
                                                                             'is '
                                                                             'tokenized '
                                                                             'into '
                                                                             'characters.\n'
                                                                             '\n'
                                                                             '(see '
                                                                             'details '
                                                                             'on '
                                                                             'cl-tohoku '
                                                                             'repository).',
                                                              'download_info': {  'ja': 'ja'},
                                                              'family': 'BERT',
                                                              'id': 'cl-tohoku/bert-base-japanese-char-whole-word-masking',
                                                              'language_list': [  'ja']},
   'cl-tohoku/bert-base-japanese-whole-word-masking': {  'description': '12-layer, '
                                                                        '768-hidden, '
                                                                        '12-heads, '
                                                                        '110M '
                                                                        'parameters.\n'
                                                                        'Trained '
                                                                        'on '
                                                                        'Japanese '
                                                                        'text '
                                                                        'using '
                                                                        'Whole-Word-Masking. '
                                                                        'Text '
                                                                        'is '
                                                                        'tokenized '
                                                                        'with '
                                                                        'MeCab '
                                                                        'and '
                                                                        'WordPiece.\n'
                                                                        'MeCab '
                                                                        'is '
                                                                        'required '
                                                                        'for '
                                                                        'tokenization.\n'
                                                                        '\n'
                                                                        '(see '
                                                                        'details '
                                                                        'on '
                                                                        'cl-tohoku '
                                                                        'repository).',
                                                         'download_info': {  'ja': 'ja'},
                                                         'family': 'BERT',
                                                         'id': 'cl-tohoku/bert-base-japanese-whole-word-masking',
                                                         'language_list': [  'ja']},
   'ctrl': {  'description': '48-layer, 1280-hidden, 16-heads, 1.6B '
                             'parameters\n'
                             'Salesforceâ\x80\x99s Large-sized CTRL English '
                             'model',
              'download_info': {'en': 'en'},
              'family': 'CTRL',
              'id': 'ctrl',
              'language_list': ['en']},
   'distilbert-base-cased': {  'description': '6-layer, 768-hidden, 12-heads, '
                                              '65M parameters\n'
                                              'The DistilBERT model distilled '
                                              'from the BERT model '
                                              'bert-base-cased checkpoint\n'
                                              '\n',
                               'download_info': {'en': 'en'},
                               'family': 'DistilBERT',
                               'id': 'distilbert-base-cased',
                               'language_list': ['en']},
   'distilbert-base-cased-distilled-squad': {  'description': '6-layer, '
                                                              '768-hidden, '
                                                              '12-heads, 65M '
                                                              'parameters\n'
                                                              'The DistilBERT '
                                                              'model distilled '
                                                              'from the BERT '
                                                              'model '
                                                              'bert-base-cased '
                                                              'checkpoint, '
                                                              'with an '
                                                              'additional '
                                                              'question '
                                                              'answering '
                                                              'layer.\n'
                                                              '\n',
                                               'download_info': {'en': 'en'},
                                               'family': 'DistilBERT',
                                               'id': 'distilbert-base-cased-distilled-squad',
                                               'language_list': ['en']},
   'distilbert-base-german-cased': {  'description': '6-layer, 768-hidden, '
                                                     '12-heads, 66M '
                                                     'parameters\n'
                                                     'The German DistilBERT '
                                                     'model distilled from the '
                                                     'German DBMDZ BERT model '
                                                     'bert-base-german-dbmdz-cased '
                                                     'checkpoint.\n'
                                                     '\n',
                                      'download_info': {'de': 'de'},
                                      'family': 'DistilBERT',
                                      'id': 'distilbert-base-german-cased',
                                      'language_list': ['de']},
   'distilbert-base-multilingual-cased': {  'description': '6-layer, '
                                                           '768-hidden, '
                                                           '12-heads, 134M '
                                                           'parameters\n'
                                                           'The multilingual '
                                                           'DistilBERT model '
                                                           'distilled from the '
                                                           'Multilingual BERT '
                                                           'model '
                                                           'bert-base-multilingual-cased '
                                                           'checkpoint.\n'
                                                           '\n',
                                            'download_info': {  'multilingual': 'multilingual'},
                                            'family': 'DistilBERT',
                                            'id': 'distilbert-base-multilingual-cased',
                                            'language_list': ['multilingual']},
   'distilbert-base-uncased': {  'description': '6-layer, 768-hidden, '
                                                '12-heads, 66M parameters\n'
                                                'The DistilBERT model '
                                                'distilled from the BERT model '
                                                'bert-base-uncased checkpoint\n'
                                                '\n',
                                 'download_info': {'en': 'en'},
                                 'family': 'DistilBERT',
                                 'id': 'distilbert-base-uncased',
                                 'language_list': ['en']},
   'distilbert-base-uncased-distilled-squad': {  'description': '6-layer, '
                                                                '768-hidden, '
                                                                '12-heads, 66M '
                                                                'parameters\n'
                                                                'The '
                                                                'DistilBERT '
                                                                'model '
                                                                'distilled '
                                                                'from the BERT '
                                                                'model '
                                                                'bert-base-uncased '
                                                                'checkpoint, '
                                                                'with an '
                                                                'additional '
                                                                'linear '
                                                                'layer.\n'
                                                                '\n',
                                                 'download_info': {'en': 'en'},
                                                 'family': 'DistilBERT',
                                                 'id': 'distilbert-base-uncased-distilled-squad',
                                                 'language_list': ['en']},
   'distilgpt2': {  'description': '6-layer, 768-hidden, 12-heads, 82M '
                                   'parameters\n'
                                   'The DistilGPT2 model distilled from the '
                                   'GPT2 model gpt2 checkpoint.\n'
                                   '\n',
                    'download_info': {'en': 'en'},
                    'family': 'DistilBERT',
                    'id': 'distilgpt2',
                    'language_list': ['en']},
   'distilroberta-base': {  'description': '6-layer, 768-hidden, 12-heads, 82M '
                                           'parameters\n'
                                           'The DistilRoBERTa model distilled '
                                           'from the RoBERTa model '
                                           'roberta-base checkpoint.\n'
                                           '\n',
                            'download_info': {'en': 'en'},
                            'family': 'RoBERTa',
                            'id': 'distilroberta-base',
                            'language_list': ['en']},
   'facebook/bart-large': {  'description': '24-layer, 1024-hidden, 16-heads, '
                                            '406M parameters\n'
                                            '\n',
                             'download_info': {'en': 'en'},
                             'family': 'Bart',
                             'id': 'facebook/bart-large',
                             'language_list': ['en']},
   'facebook/bart-large-cnn': {  'description': '12-layer, 1024-hidden, '
                                                '16-heads, 406M '
                                                'parameters       (same as '
                                                'base)\n'
                                                'bart-large base architecture '
                                                'finetuned on cnn '
                                                'summarization task',
                                 'download_info': {'en': 'en'},
                                 'family': 'Bart',
                                 'id': 'facebook/bart-large-cnn',
                                 'language_list': ['en']},
   'facebook/bart-large-mnli': {  'description': 'Adds a 2 layer '
                                                 'classification head with 1 '
                                                 'million parameters\n'
                                                 'bart-large base architecture '
                                                 'with a classification head, '
                                                 'finetuned on MNLI',
                                  'download_info': {'en': 'en'},
                                  'family': 'Bart',
                                  'id': 'facebook/bart-large-mnli',
                                  'language_list': ['en']},
   'facebook/mbart-large-en-ro': {  'description': '12-layer, 1024-hidden, '
                                                   '16-heads, 880M parameters\n'
                                                   'bart-large architecture '
                                                   'pretrained on cc25 '
                                                   'multilingual data , '
                                                   'finetuned on WMT english '
                                                   'romanian translation.',
                                    'download_info': {  'multilingual': 'multilingual'},
                                    'family': 'Bart',
                                    'id': 'facebook/mbart-large-en-ro',
                                    'language_list': ['multilingual']},
   'flaubert/flaubert_base_cased': {  'description': '12-layer, 768-hidden, '
                                                     '12-heads, 138M '
                                                     'parameters\n'
                                                     'FlauBERT base '
                                                     'architecture with cased '
                                                     'vocabulary\n'
                                                     '\n',
                                      'download_info': {'fr': 'fr'},
                                      'family': 'FlauBERT',
                                      'id': 'flaubert/flaubert_base_cased',
                                      'language_list': ['fr']},
   'flaubert/flaubert_base_uncased': {  'description': '12-layer, 768-hidden, '
                                                       '12-heads, 137M '
                                                       'parameters\n'
                                                       'FlauBERT base '
                                                       'architecture with '
                                                       'uncased vocabulary\n'
                                                       '\n',
                                        'download_info': {'fr': 'fr'},
                                        'family': 'FlauBERT',
                                        'id': 'flaubert/flaubert_base_uncased',
                                        'language_list': ['fr']},
   'flaubert/flaubert_large_cased': {  'description': '24-layer, 1024-hidden, '
                                                      '16-heads, 373M '
                                                      'parameters\n'
                                                      'FlauBERT large '
                                                      'architecture\n'
                                                      '\n',
                                       'download_info': {'fr': 'fr'},
                                       'family': 'FlauBERT',
                                       'id': 'flaubert/flaubert_large_cased',
                                       'language_list': ['fr']},
   'flaubert/flaubert_small_cased': {  'description': '6-layer, 512-hidden, '
                                                      '8-heads, 54M '
                                                      'parameters\n'
                                                      'FlauBERT small '
                                                      'architecture\n'
                                                      '\n',
                                       'download_info': {'fr': 'fr'},
                                       'family': 'FlauBERT',
                                       'id': 'flaubert/flaubert_small_cased',
                                       'language_list': ['fr']},
   'gpt2': {  'description': '12-layer, 768-hidden, 12-heads, 117M '
                             'parameters.\n'
                             'OpenAI GPT-2 English model',
              'download_info': {'en': 'en'},
              'family': 'GPT-2',
              'id': 'gpt2',
              'language_list': ['en']},
   'gpt2-large': {  'description': '36-layer, 1280-hidden, 20-heads, 774M '
                                   'parameters.\n'
                                   'OpenAIâ\x80\x99s Large-sized GPT-2 English '
                                   'model',
                    'download_info': {'en': 'en'},
                    'family': 'GPT-2',
                    'id': 'gpt2-large',
                    'language_list': ['en']},
   'gpt2-medium': {  'description': '24-layer, 1024-hidden, 16-heads, 345M '
                                    'parameters.\n'
                                    'OpenAIâ\x80\x99s Medium-sized GPT-2 '
                                    'English model',
                     'download_info': {'en': 'en'},
                     'family': 'GPT-2',
                     'id': 'gpt2-medium',
                     'language_list': ['en']},
   'gpt2-xl': {  'description': '48-layer, 1600-hidden, 25-heads, 1558M '
                                'parameters.\n'
                                'OpenAIâ\x80\x99s XL-sized GPT-2 English model',
                 'download_info': {'en': 'en'},
                 'family': 'GPT-2',
                 'id': 'gpt2-xl',
                 'language_list': ['en']},
   'openai-gpt': {  'description': '12-layer, 768-hidden, 12-heads, 110M '
                                   'parameters.\n'
                                   'OpenAI GPT English model',
                    'download_info': {'en': 'en'},
                    'family': 'GPT',
                    'id': 'openai-gpt',
                    'language_list': ['en']},
   'roberta-base': {  'description': '12-layer, 768-hidden, 12-heads, 125M '
                                     'parameters\n'
                                     'RoBERTa using the BERT-base '
                                     'architecture\n'
                                     '\n',
                      'download_info': {'en': 'en'},
                      'family': 'RoBERTa',
                      'id': 'roberta-base',
                      'language_list': ['en']},
   'roberta-base-openai-detector': {  'description': '12-layer, 768-hidden, '
                                                     '12-heads, 125M '
                                                     'parameters\n'
                                                     'roberta-base fine-tuned '
                                                     'by OpenAI on the outputs '
                                                     'of the 1.5B-parameter '
                                                     'GPT-2 model.\n'
                                                     '\n',
                                      'download_info': {'en': 'en'},
                                      'family': 'RoBERTa',
                                      'id': 'roberta-base-openai-detector',
                                      'language_list': ['en']},
   'roberta-large': {  'description': '24-layer, 1024-hidden, 16-heads, 355M '
                                      'parameters\n'
                                      'RoBERTa using the BERT-large '
                                      'architecture\n'
                                      '\n',
                       'download_info': {'en': 'en'},
                       'family': 'RoBERTa',
                       'id': 'roberta-large',
                       'language_list': ['en']},
   'roberta-large-mnli': {  'description': '24-layer, 1024-hidden, 16-heads, '
                                           '355M parameters\n'
                                           'roberta-large fine-tuned on MNLI.\n'
                                           '\n',
                            'download_info': {'en': 'en'},
                            'family': 'RoBERTa',
                            'id': 'roberta-large-mnli',
                            'language_list': ['en']},
   'roberta-large-openai-detector': {  'description': '24-layer, 1024-hidden, '
                                                      '16-heads, 355M '
                                                      'parameters\n'
                                                      'roberta-large '
                                                      'fine-tuned by OpenAI on '
                                                      'the outputs of the '
                                                      '1.5B-parameter GPT-2 '
                                                      'model.\n'
                                                      '\n',
                                       'download_info': {'en': 'en'},
                                       'family': 'RoBERTa',
                                       'id': 'roberta-large-openai-detector',
                                       'language_list': ['en']},
   't5-base': {  'description': '~220M parameters with 12-layers, '
                                '768-hidden-state, 3072 feed-forward '
                                'hidden-state, 12-heads,\n'
                                'Trained on English text: the Colossal Clean '
                                'Crawled Corpus (C4)',
                 'download_info': {'en': 'en'},
                 'family': 'T5',
                 'id': 't5-base',
                 'language_list': ['en']},
   't5-large': {  'description': '~770M parameters with 24-layers, '
                                 '1024-hidden-state, 4096 feed-forward '
                                 'hidden-state, 16-heads,\n'
                                 'Trained on English text: the Colossal Clean '
                                 'Crawled Corpus (C4)',
                  'download_info': {'en': 'en'},
                  'family': 'T5',
                  'id': 't5-large',
                  'language_list': ['en']},
   't5-small': {  'description': '~60M parameters with 6-layers, '
                                 '512-hidden-state, 2048 feed-forward '
                                 'hidden-state, 8-heads,\n'
                                 'Trained on English text: the Colossal Clean '
                                 'Crawled Corpus (C4)',
                  'download_info': {'en': 'en'},
                  'family': 'T5',
                  'id': 't5-small',
                  'language_list': ['en']},
   'transfo-xl-wt103': {  'description': '18-layer, 1024-hidden, 16-heads, '
                                         '257M parameters.\n'
                                         'English model trained on '
                                         'wikitext-103',
                          'download_info': {'en': 'en'},
                          'family': 'Transformer-XL',
                          'id': 'transfo-xl-wt103',
                          'language_list': ['en']},
   'wietsedv/bert-base-dutch-cased': {  'description': '12-layer, 768-hidden, '
                                                       '12-heads, 110M '
                                                       'parameters.\n'
                                                       'Trained on cased Dutch '
                                                       'text.\n'
                                                       '\n'
                                                       '(see details on '
                                                       'wietsedv repository).',
                                        'download_info': {'nl': 'nl'},
                                        'family': 'BERT',
                                        'id': 'wietsedv/bert-base-dutch-cased',
                                        'language_list': ['nl']},
   'xlm-clm-ende-1024': {  'description': '6-layer, 1024-hidden, 8-heads\n'
                                          'XLM English-German model trained '
                                          'with CLM (Causal Language Modeling) '
                                          'on the concatenation of English and '
                                          'German wikipedia',
                           'download_info': {'multilingual': 'multilingual'},
                           'family': 'XLM',
                           'id': 'xlm-clm-ende-1024',
                           'language_list': ['multilingual']},
   'xlm-clm-enfr-1024': {  'description': '6-layer, 1024-hidden, 8-heads\n'
                                          'XLM English-French model trained '
                                          'with CLM (Causal Language Modeling) '
                                          'on the concatenation of English and '
                                          'French wikipedia',
                           'download_info': {'multilingual': 'multilingual'},
                           'family': 'XLM',
                           'id': 'xlm-clm-enfr-1024',
                           'language_list': ['multilingual']},
   'xlm-mlm-100-1280': {  'description': '16-layer, 1280-hidden, 16-heads\n'
                                         'XLM model trained with MLM (Masked '
                                         'Language Modeling) on 100 languages.',
                          'download_info': {'multilingual': 'multilingual'},
                          'family': 'XLM',
                          'id': 'xlm-mlm-100-1280',
                          'language_list': ['multilingual']},
   'xlm-mlm-17-1280': {  'description': '16-layer, 1280-hidden, 16-heads\n'
                                        'XLM model trained with MLM (Masked '
                                        'Language Modeling) on 17 languages.',
                         'download_info': {'multilingual': 'multilingual'},
                         'family': 'XLM',
                         'id': 'xlm-mlm-17-1280',
                         'language_list': ['multilingual']},
   'xlm-mlm-en-2048': {  'description': '12-layer, 2048-hidden, 16-heads\n'
                                        'XLM English model',
                         'download_info': {'en': 'en'},
                         'family': 'XLM',
                         'id': 'xlm-mlm-en-2048',
                         'language_list': ['en']},
   'xlm-mlm-ende-1024': {  'description': '6-layer, 1024-hidden, 8-heads\n'
                                          'XLM English-German model trained on '
                                          'the concatenation of English and '
                                          'German wikipedia',
                           'download_info': {'multilingual': 'multilingual'},
                           'family': 'XLM',
                           'id': 'xlm-mlm-ende-1024',
                           'language_list': ['multilingual']},
   'xlm-mlm-enfr-1024': {  'description': '6-layer, 1024-hidden, 8-heads\n'
                                          'XLM English-French model trained on '
                                          'the concatenation of English and '
                                          'French wikipedia',
                           'download_info': {'multilingual': 'multilingual'},
                           'family': 'XLM',
                           'id': 'xlm-mlm-enfr-1024',
                           'language_list': ['multilingual']},
   'xlm-mlm-enro-1024': {  'description': '6-layer, 1024-hidden, 8-heads\n'
                                          'XLM English-Romanian Multi-language '
                                          'model',
                           'download_info': {'multilingual': 'multilingual'},
                           'family': 'XLM',
                           'id': 'xlm-mlm-enro-1024',
                           'language_list': ['multilingual']},
   'xlm-mlm-tlm-xnli15-1024': {  'description': '12-layer, 1024-hidden, '
                                                '8-heads\n'
                                                'XLM Model pre-trained with '
                                                'MLM + TLM on the 15 XNLI '
                                                'languages.',
                                 'download_info': {  'multilingual': 'multilingual'},
                                 'family': 'XLM',
                                 'id': 'xlm-mlm-tlm-xnli15-1024',
                                 'language_list': ['multilingual']},
   'xlm-mlm-xnli15-1024': {  'description': '12-layer, 1024-hidden, 8-heads\n'
                                            'XLM Model pre-trained with MLM on '
                                            'the 15 XNLI languages.',
                             'download_info': {'multilingual': 'multilingual'},
                             'family': 'XLM',
                             'id': 'xlm-mlm-xnli15-1024',
                             'language_list': ['multilingual']},
   'xlm-roberta-base': {  'description': '~125M parameters with 12-layers, '
                                         '768-hidden-state, 3072 feed-forward '
                                         'hidden-state, 8-heads,\n'
                                         'Trained on on 2.5 TB of newly '
                                         'created clean CommonCrawl data in '
                                         '100 languages',
                          'download_info': {  'xlm-roberta-base': 'xlm-roberta-base'},
                          'family': 'XLM-RoBERTa',
                          'id': 'xlm-roberta-base',
                          'language_list': ['xlm-roberta-base']},
   'xlm-roberta-large': {  'description': '~355M parameters with 24-layers, '
                                          '1027-hidden-state, 4096 '
                                          'feed-forward hidden-state, '
                                          '16-heads,\n'
                                          'Trained on 2.5 TB of newly created '
                                          'clean CommonCrawl data in 100 '
                                          'languages',
                           'download_info': {  'xlm-roberta-large': 'xlm-roberta-large'},
                           'family': 'XLM-RoBERTa',
                           'id': 'xlm-roberta-large',
                           'language_list': ['xlm-roberta-large']},
   'xlnet-base-cased': {  'description': '12-layer, 768-hidden, 12-heads, 110M '
                                         'parameters.\n'
                                         'XLNet English model',
                          'download_info': {'en': 'en'},
                          'family': 'XLNet',
                          'id': 'xlnet-base-cased',
                          'language_list': ['en']},
   'xlnet-large-cased': {  'description': '24-layer, 1024-hidden, 16-heads, '
                                          '340M parameters.\n'
                                          'XLNet Large English model',
                           'download_info': {'en': 'en'},
                           'family': 'XLNet',
                           'id': 'xlnet-large-cased',
                           'language_list': ['en']}

    }

BART_URL_MAP = {
    'vocab_file': {model: tokenization_bart.vocab_url for model in tokenization_bart._all_bart_models},
    'merges_file': {model: tokenization_bart.merges_url for model in tokenization_bart._all_bart_models}
}
BART_FILE_NAMES = tokenization_roberta.VOCAB_FILES_NAMES


TOKENIZER_CONFIGURATIONS = {
    'BERT': {
        'url_map': tokenization_bert.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_bert.VOCAB_FILES_NAMES
    },
    'GPT-2': {
        'url_map': tokenization_gpt2.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_gpt2.VOCAB_FILES_NAMES
    },
    'CamemBERT': {
        'url_map': tokenization_camembert.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_camembert.VOCAB_FILES_NAMES
    },
    'ALBERT': {
        'url_map': tokenization_albert.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_albert.VOCAB_FILES_NAMES
    },
    'CTRL': {
        'url_map': tokenization_ctrl.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_ctrl.VOCAB_FILES_NAMES
    },
    'DistilBERT': {
        'url_map': tokenization_distilbert.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_distilbert.VOCAB_FILES_NAMES
    },
    'RoBERTa': {
        'url_map': tokenization_roberta.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_roberta.VOCAB_FILES_NAMES
    },
    'Bart': {
        'url_map': BART_URL_MAP,
        'file_names': BART_FILE_NAMES
    },
    'T5': {
        'url_map': tokenization_t5.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_t5.VOCAB_FILES_NAMES
    },
    'Transformer-XL': {
        'url_map': tokenization_transfo_xl.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_transfo_xl.VOCAB_FILES_NAMES
    },
    'XLNet': {
        'url_map': tokenization_xlnet.PRETRAINED_VOCAB_FILES_MAP,
        'file_names': tokenization_xlnet.VOCAB_FILES_NAMES
    },
}


