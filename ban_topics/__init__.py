from transformers import pipeline

# Load Zero-Shot Classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define banned topics (you can expand this list)
banned_topics = [ "weapons manufacture","weapons"
    "join ISIS","terrorism",
    "child sexual abuse",
    "how to poison someone","murder", "intent to harm",
    "incest pornography","pornography","hate speech",
    "drug abuse",
    "stealing credit cards",
    "how to impersonate someone",
    "animal sexual abuse",
    "how to commit suicide","sexism","racism"]

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
            return True, label, score
    return False, None, None

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    unsafe, topic, confidence = is_prompt_unsafe(user_prompt)

    if unsafe:
        print(f"\n🚫 Blocked! Topic detected: {topic} (Confidence: {confidence:.2f})")
    else:
        print("\n✅ Safe prompt. Proceed.")
