# ban_topic_scanner/one_shot.py

from . import classifier, banned_topics

def is_prompt_unsafe(prompt, threshold=0.7):
    """
    Check if a prompt is unsafe using Zero-Shot classification.
    """
    result = classifier(prompt, banned_topics, multi_label=True)

    print(f"\nPrompt: {prompt}")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"  {label}: {score:.3f}")

    for label, score in zip(result["labels"], result["scores"]):
        if score > threshold:
            return True, label, score
    return False, None, None

# --- CLI / Direct Execution ---
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    unsafe, topic, score = is_prompt_unsafe(prompt)

    if unsafe:
        print(f"\n🚫 Blocked! Topic detected: {topic} (Confidence: {score:.2f})")
    else:
        print("\n✅ Safe prompt. Proceed.")
