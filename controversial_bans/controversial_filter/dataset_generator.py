import pandas as pd
import numpy as np
from faker import Faker
import re

def extract_keywords(text):
    """Extracts meaningful keywords from a given question."""
    stop_words = {"is", "the", "why", "should", "what", "how", "who", "in", "of", "to", "does"}  # Common words to ignore
    words = re.findall(r'\b\w+\b', text.lower())  # Tokenize text
    keywords = [word for word in words if word not in stop_words]
    return ", ".join(keywords)  # Convert list to comma-separated string

def generate_controversial_dataset(num_entries=2500):
    fake = Faker('en_IN')  # For Indian context
    
    # Categories of controversial/comparative topics in Indian context
    categories = {
        'religion': [
            "Why is {religion1} better than {religion2}?",
            "Should {religion} be banned in India?",
            "Is {religion} the true religion?",
            "Why do {religion} followers behave like {negative_adj}?"
        ],
        'politics': [
            "Is {party1} better than {party2}?",
            "Why is {leader1} superior to {leader2}?",
            "Should {party} be banned in India?",
            "Why does {party} always do {negative_adj} things?"
        ],
        'regional': [
            "Why are people from {state1} better than {state2}?",
            "Is {language1} superior to {language2}?",
            "Why does {state} always cause problems?",
            "Should {state} be separated from India?"
        ]
    }

    # Indian-specific data
    religions = ["Hinduism", "Islam", "Christianity", "Sikhism", "Buddhism", "Jainism"]
    parties = ["BJP", "Congress", "AAP", "TMC", "Shiv Sena", "DMK"]
    leaders = ["Modi", "Gandhi", "Kejriwal", "Mamata", "Thackeray", "Stalin"]
    states = ["Kerala", "UP", "Bihar", "Tamil Nadu", "Punjab", "Gujarat"]
    languages = ["Hindi", "Tamil", "Bengali", "Punjabi", "Malayalam", "Telugu"]
    negative_adjs = ["bad", "wrong", "evil", "violent", "corrupt"]

    dataset = []
    for _ in range(num_entries):
        category = np.random.choice(list(categories.keys()))
        template = np.random.choice(categories[category])
        
        question = template.format(
            religion1=np.random.choice(religions),
            religion2=np.random.choice([r for r in religions if r != 'religion1']),
            religion=np.random.choice(religions),
            party1=np.random.choice(parties),
            party2=np.random.choice([p for p in parties if p != 'party1']),
            party=np.random.choice(parties),
            leader1=np.random.choice(leaders),
            leader2=np.random.choice([l for l in leaders if l != 'leader1']),
            state1=np.random.choice(states),
            state2=np.random.choice([s for s in states if s != 'state1']),
            state=np.random.choice(states),
            language1=np.random.choice(languages),
            language2=np.random.choice([l for l in languages if l != 'language1']),
            negative_adj=np.random.choice(negative_adjs)
        )
        
        dataset.append({
            'question': question,
            'category': category,
            'is_controversial': True,
            'keywords': extract_keywords(question)  # Generate keywords from question
        })
    
    # Add non-controversial questions
    non_controversial = [
        "What is the capital of India?",
        "How to make chai?",
        "What are the major festivals in India?",
        "Explain the Indian education system",
        "What are popular tourist places in India?"
    ]
    
    for q in non_controversial:
        dataset.append({
            'question': q,
            'category': 'general',
            'is_controversial': False,
            'keywords': extract_keywords(q)  # Generate keywords for non-controversial questions
        })
    
    # Shuffle and save
    df = pd.DataFrame(dataset)
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_csv('controversial_topics.csv', index=False)
    return df

if __name__ == "__main__":
    print("Generating dataset...")
    df = generate_controversial_dataset(2500)
    print(f"✅ Dataset generated with {len(df)} entries. Saved to controversial_topics.csv")
    print(df.head())  # Show first few rows to verify
