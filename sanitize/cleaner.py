import re

# Dictionary of PII detection patterns
PII_PATTERNS = {
    "EMAIL": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "PHONE": re.compile(r"\b\d{10}\b|\b\d{3}[- ]\d{3}[- ]\d{4}\b"),
    "IP_ADDRESS": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "CREDIT_CARD": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "DATE": re.compile(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b")
}

def sanitize_text(text):
    """
    Replaces PII values with placeholder tags like [EMAIL], [PHONE], etc.
    """
    for pii_type, pattern in PII_PATTERNS.items():
        text = pattern.sub(f"[{pii_type}]", text)
    return text
# input_text = """
# Hi, my name is John Doe. You can email me at john.doe@example.com or call 123-456-7890.
# My SSN is 123-45-6789 and I was born on 01/01/1990. Also, my IP address is 192.168.1.1.
# """
# output = sanitize_text(input_text)
# print(output)
# Hi, my name is John Doe. You can email me at [EMAIL] or call [PHONE].
# My SSN is [SSN] and I was born on [DATE]. Also, my IP address is [IP_ADDRESS].
