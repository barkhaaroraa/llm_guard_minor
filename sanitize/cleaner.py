import re

def sanitize_text(text):
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL]", text)
    text = re.sub(r"\b\d{10}\b", "[PHONE]", text)
    text = re.sub(r"\b\d{3} \d{3} \d{4}\b", "[PHONE]", text)
    return text
