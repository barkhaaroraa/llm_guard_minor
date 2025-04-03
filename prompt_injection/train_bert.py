import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from data_preprocessing import PromptDataset  # Ensure this is correctly imported

# Print to check if script starts
print("train_bert.py is running...")

# Allow PyTorch to recognize the PromptDataset class
torch.serialization.add_safe_globals([PromptDataset])

# Load dataset
print("Loading datasets...")
train_dataset = torch.load("train_dataset.pt", weights_only=False)
test_dataset = torch.load("test_dataset.pt", weights_only=False)

# Print dataset sizes
print(f"Train samples: {len(train_dataset)}")
print(f"Test samples: {len(test_dataset)}")
train_attack = sum(train_dataset.labels)
train_safe = len(train_dataset.labels) - train_attack

test_attack = sum(test_dataset.labels)
test_safe = len(test_dataset.labels) - test_attack
print(f"Train Attack: {train_attack}, Train Safe: {train_safe}")
print(f"Test Attack: {test_attack}, Test Safe: {test_safe}")    
# # Load BERT model
# model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# # Training parameters
# training_args = TrainingArguments(
#     output_dir="./results",
#     num_train_epochs=3,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     warmup_steps=500,
#     weight_decay=0.01,
#     evaluation_strategy="epoch",
#     logging_dir="./logs",
# )

# # Trainer object
# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_dataset,
#     eval_dataset=test_dataset,
# )

# # Train model
# print("Starting training...")
# trainer.train()
# print("Training completed!")

# # Evaluate model
# results = trainer.evaluate()
# print("Evaluation Results:", results)

# # Save model and tokenizer
# model.save_pretrained("./llmguard_bert")
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# tokenizer.save_pretrained("./llmguard_bert")

# print("Training complete! Model saved in './llmguard_bert'.")
