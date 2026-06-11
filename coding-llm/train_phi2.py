from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_name)

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

dataset = load_dataset(
    "json",
    data_files="expanded_dataset.jsonl"
)["train"]

def tokenize(example):

    text = (
        f"Instruction: {example['instruction']}\n"
        f"Answer: {example['output']}"
    )

    return tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128
    )

tokenized = dataset.map(tokenize)

# Use only 20 records for a fast test run on CPU
tokenized = tokenized.select(range(min(20, len(tokenized))))
print(f"Training on {len(tokenized)} records (test run)")

training_args = TrainingArguments(
    output_dir="./tinyllama-coding-model",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    logging_steps=1,
    save_steps=10,
    learning_rate=2e-4,
    report_to="none",
    use_cpu=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    data_collator=DataCollatorForLanguageModeling(
        tokenizer,
        mlm=False
    )
)

trainer.train()

model.save_pretrained("./tinyllama-coding-model")
tokenizer.save_pretrained("./tinyllama-coding-model")

print("MODEL SAVED SUCCESSFULLY")