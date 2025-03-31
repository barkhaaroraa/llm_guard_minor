import torch
from torch.utils.data import DataLoader
from transformers import BertForSequenceClassification, BertTokenizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from data_preprocessing import PromptDataset  # Ensure this is correctly imported
import os

# Allowlist the necessary global classes for safe loading
torch.serialization.add_safe_globals(["transformers.tokenization_utils_base.BatchEncoding"])

# Load the tokenizer and model
model_path = "./llmguard_bert"  # Make sure this path is correct
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

# Load the test dataset
# Load test dataset (Ensure it is an instance of PromptDataset)
test_data = torch.load("test_dataset.pt", weights_only=False)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# Extract input_ids, attention_mask, and labels properly
test_loader = DataLoader(test_data, batch_size=8, shuffle=False)

true_labels = []
predictions = []

# Perform inference batch-wise
model.eval()
with torch.no_grad():
    for batch in test_loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=1)

        true_labels.extend(labels.cpu().numpy())
        predictions.extend(preds.cpu().numpy())

# Compute evaluation metrics
accuracy = accuracy_score(true_labels, predictions)
precision = precision_score(true_labels, predictions, zero_division=1)
recall = recall_score(true_labels, predictions, zero_division=1)
f1 = f1_score(true_labels, predictions, zero_division=1)

print("📊 Model Evaluation Results:")
print(f"✅ Accuracy:  {accuracy:.4f}")
print(f"🎯 Precision: {precision:.4f}")
print(f"🔍 Recall:    {recall:.4f}")
print(f"📈 F1-score:  {f1:.4f}")
