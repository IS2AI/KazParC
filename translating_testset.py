# Define the GPU

from datetime import datetime
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Import the model

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained('./tilmash/', local_files_only=True).to('cuda')
print('Model is ready')

# Import test dataset

import json
with open('14_kazparc_test_set.json') as file:
    dataset = json.load(file)

# Function for text translation

def translation(data, src_lang, trg_lang):
    languages = {'ru': 'rus_Cyrl', 'kk': 'kaz_Cyrl', 'en': 'eng_Latn', 'tr': 'tur_Latn'}
    src_tok = languages[src_lang]
    tokenizer = AutoTokenizer.from_pretrained('./tilmash/', local_files_only=True, src_lang=src_tok)
    start = datetime.now()
    print(start, src_tok, trg_lang)
    for n, row in enumerate(data):
        if n % 100 == 0:
            print(f'Checkpoint: {n}. Time: {datetime.now()}')
        inputs = tokenizer(row[src_lang], return_tensors="pt").to('cuda')
        translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[trg_lang]).to('cuda')
        trans = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        truncated = trg_lang[:2]
        name = 'trans_' + src_lang + '_' + truncated
        row[name] = trans
    df = pd.DataFrame(data)
    lang_code = name[6:]
    dataset_name = 'tilmash_' + lang_code + '.json'
    df.to_json(dataset_name, orient='records', force_ascii=False)
    return None

# Translate test dataset

if __name__=="__main__":
    translation(dataset, 'kk', 'eng_Latn')
    translation(dataset, 'kk', 'rus_Cyrl')
    translation(dataset, 'kk', 'tur_Latn')
    translation(dataset, 'ru', 'eng_Latn')
    translation(dataset, 'ru', 'kaz_Cyrl')
    translation(dataset, 'ru', 'tur_Latn')
    translation(dataset, 'en', 'kaz_Cyrl')
    translation(dataset, 'en', 'rus_Cyrl')
    translation(dataset, 'en', 'tur_Latn')
    translation(dataset, 'tr', 'eng_Latn')
    translation(dataset, 'tr', 'kaz_Cyrl')
    translation(dataset, 'tr', 'rus_Cyrl')
