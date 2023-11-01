from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained('./tilmash/')

def translate():
    src = str(input('Source language: '))
    trg = str(input('Target language: '))
    text = str(input())
    tokenizer = AutoTokenizer.from_pretrained('./tilmash/', src_lang=src)
    inputs = tokenizer(text, return_tensors='pt')
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[trg], max_length=1000)
    translated_sentence = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)
    translated_sentence = translated_sentence[0]
    return translated_sentence

trans_text = translate()
print(trans_text)
