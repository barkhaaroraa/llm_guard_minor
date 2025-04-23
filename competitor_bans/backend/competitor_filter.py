# competitor_filter.py

from intent_model import predict_intent

# List of blocked labels
BLOCKED_INTENTS = ['competitor']

# Harmless keywords that shouldn't trigger competitor filter
HARMLESS_KEYWORDS = {'icecream', 'ice cream', 'chocolate', 'vanilla', 
                     'food', 'restaurant', 'movie', 'music', 'sport','computer'}

def is_query_blocked(user_input):
    """
    Returns True if the query should be blocked (e.g., competitor intent),
    otherwise returns False.
    """
    # First check for obviously harmless content
    if any(keyword in user_input.lower() for keyword in HARMLESS_KEYWORDS):
        return False
        
    intent = predict_intent(user_input)
    print(f"[INFO] Detected intent: {intent}")
    
    return intent in BLOCKED_INTENTS


# Optional: demo usage
if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        if query.lower() == 'exit':
            break
        if is_query_blocked(query):
            print("🚫 Query blocked (competitor intent).")
        else:
            print("✅ Query allowed.")