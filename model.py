import torch
import torch.nn as nn
from transformers import BertModel

class BertForPromptInjection(nn.Module):
    def __init__(self):
        super(BertForPromptInjection, self).__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")  # Load pre-trained BERT
        self.dropout = nn.Dropout(0.3)  # Add dropout to reduce overfitting
        self.fc = nn.Linear(self.bert.config.hidden_size, 2)  # Output layer (binary classification)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output  # Use the CLS token representation
        x = self.dropout(pooled_output)
        logits = self.fc(x)  # Output logits for two classes (safe or injected)
        return logits
