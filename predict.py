import torch
from transformers import BertForSequenceClassification, BertTokenizer

# Load trained model and tokenizer
model_path = "./llmguard_bert"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

# Move model to CPU (since you don’t have a GPU)
device = torch.device("cpu")
model.to(device)

# Function to predict if a prompt is an injection attack
def predict_prompt(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}  # Move to CPU

    with torch.no_grad():  # Disable gradient calculation
        outputs = model(**inputs)

    prediction = torch.argmax(outputs.logits, dim=1).item()
    return "🚨 Injection Attack Detected!" if prediction == 1 else "✅ Safe Prompt"

# Continuous user input loop
while True:
    user_input = input("\nEnter a prompt (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    print(f"Prediction: {predict_prompt(user_input)}")
