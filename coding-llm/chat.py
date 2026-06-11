from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = "./tinyllama-coding-model"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
print("Model loaded! Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    text = f"Instruction: {prompt}\nAnswer:"
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            do_sample=True,
            repetition_penalty=1.15,
            pad_token_id=tokenizer.eos_token_id
        )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nAI:", result.replace(text, "").strip())
    print()
