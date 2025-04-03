import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer


df = pd.read_csv("prompt_injections.csv")

# Ensure correct column names
df = df.rename(columns={"text_column_name": "text", "label_column_name": "label"})

# Split dataset
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["text"].tolist(), df["label"].tolist(), test_size=0.2, random_state=42
)

# Load BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize data
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=512)

# Convert to PyTorch Dataset
class PromptDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "input_ids": torch.tensor(self.encodings["input_ids"][idx]),
            "attention_mask": torch.tensor(self.encodings["attention_mask"][idx]),
            "labels": torch.tensor(self.labels[idx]),
        }

# Save datasets
train_dataset = PromptDataset(train_encodings, train_labels)
test_dataset = PromptDataset(test_encodings, test_labels)

torch.save(train_dataset, "train_dataset.pt")
torch.save(test_dataset, "test_dataset.pt")

print("✅ Data preprocessing complete. Train & test datasets saved!")
