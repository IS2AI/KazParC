import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_from_disk
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
import tensorflow as tf
import torch

# Import the baseline model

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-1.3B")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-1.3B")
print('Model is ready!')

# Import the train and dev sets

df_train = load_from_disk('./kazparc_synt_train/')
df_dev = load_from_disk('./kazparc_synt_dev/')
print('Dataset is ready!')

# Define the parameters

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

training_args = Seq2SeqTrainingArguments(
    output_dir="tilmash_checkpoints",
    optim='adafactor',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    prediction_loss_only=True,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    gradient_accumulation_steps=32,
    eval_accumulation_steps=32,
    save_total_limit=2,
    num_train_epochs=3,
    predict_with_generate=True,
    generation_max_length=256,
    push_to_hub=False,
    fp16=True)

trainer = Seq2SeqTrainer(
    model=model,
    data_collator=data_collator,
    args=training_args,
    train_dataset=df_train,
    eval_dataset=df_dev,
    tokenizer=tokenizer,
    compute_metrics=False)

# Start to training a model

trainer.train()

# Save the model

pt_save_directory = "tilmash"
tokenizer.save_pretrained(pt_save_directory)
model.save_pretrained(pt_save_directory)

