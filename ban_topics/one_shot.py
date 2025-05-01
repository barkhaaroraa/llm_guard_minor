from transformers import pipeline

# Load Zero-Shot Classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define banned topics (you can expand this list)
banned_topics = [ "animal sexual abuse", "sexism","racism"]

def is_prompt_unsafe(prompt, threshold=0.7):
    """
    Classify prompt against banned topics.
    Returns True if classified as a banned topic above the threshold.
    """
    result = classifier(prompt, banned_topics, multi_label=True)

    # Print classification results (optional)
    print(f"\nPrompt: {prompt}")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"  {label}: {score:.3f}")

    # Decision: if any banned topic exceeds the threshold
    for label, score in zip(result["labels"], result["scores"]):
        if score > threshold:
            return True
    return False
