# intent_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Paths
DATA_PATH = "backend/data/intents.csv"
MODEL_PATH = "backend/models/intent_model.pkl"

def train_and_save_model():
    # Load dataset
    df = pd.read_csv(DATA_PATH)
    
    # Split features and labels
    X = df['text']
    y = df['label']
    
    # Build pipeline (vectorizer + classifier)
    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', LogisticRegression(max_iter=1000))
    ])
    
    # Train model
    model.fit(X, y)
    
    # Create model folder if it doesn't exist
    os.makedirs("models", exist_ok=True)
    
    # Save the trained pipeline
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_intent(text):
    model = load_model()
    return model.predict([text])[0]

if __name__ == "__main__":
    train_and_save_model()
