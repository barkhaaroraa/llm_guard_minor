import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ControversialFilter:
    def __init__(self, dataset_path=r"C:\Users\Nishtha Kanyal\OneDrive\Desktop\coding\python\llm_guard_minor\controversial_bans\controversial_filter\controversial_topics.csv"):
        try:
            df = pd.read_csv(dataset_path)
            df.columns = df.columns.str.strip()  # Trim spaces from column names
            
            print("\u2705 Dataset loaded successfully.")
            print(df.head())  # Print first few rows to check
            print(df.columns)  # Print column names
            
            if "keywords" not in df.columns:
                raise KeyError("Column 'keywords' not found in dataset!")

            self.controversial_keywords = df["keywords"].dropna().tolist()
            print("Extracted Keywords:", self.controversial_keywords[:10])  # Print first few keywords

            if not self.controversial_keywords:
                print("Warning: No keywords found in dataset!")

            # Compile regex pattern from controversial keywords
            self.keyword_patterns = re.compile(r"\\b(" + "|".join(map(re.escape, self.controversial_keywords)) + r")\\b", re.IGNORECASE)

            # Initialize TF-IDF Vectorizer for similarity checking
            self.vectorizer = TfidfVectorizer()
            self.question_vectors = self.vectorizer.fit_transform(self.controversial_keywords)

        except FileNotFoundError:
            raise FileNotFoundError(f"Dataset not found at {dataset_path}. Please generate it first.")
        except KeyError as e:
            print(str(e))

    def contains_keywords(self, text):
        """Check if text contains controversial keywords"""
        return bool(self.keyword_patterns.search(text))

    def is_similar_to_known(self, text, threshold=0.7):
        """Check if input text is similar to known controversial questions"""
        input_vector = self.vectorizer.transform([text])
        similarities = cosine_similarity(input_vector, self.question_vectors)
        return similarities.max() > threshold

    def is_controversial(self, text):
        """Check if text is controversial based on keywords and similarity"""
        if self.contains_keywords(text):
            return True
        if self.is_similar_to_known(text):
            return True
        return False

if __name__ == "__main__":
    filter = ControversialFilter()
    test_text = "Should BJP be banned in India?"
    print(f"Is the text controversial? {filter.is_controversial(test_text)}")
