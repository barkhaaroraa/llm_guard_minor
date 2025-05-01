# ban_topic_scanner/__init__.py

from transformers import pipeline

# Initialize Zero-Shot Classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Centralized banned topic list
banned_topics = [
    "weapons manufacture", "weapons",
    "join ISIS", "terrorism","child abuse"
    "child sexual abuse",
    "how to poison someone", "murder", "intent to harm",
    "incest pornography", "pornography", "hate speech",
    "drug abuse",
    "stealing credit cards",
    "how to impersonate someone","animal abuse",
    "animal sexual abuse",
    "how to commit suicide", "sexism", "racism"
]
