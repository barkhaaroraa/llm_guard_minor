from datasets import load_dataset
import pandas as pd

# Load the dataset
print("Loading dataset...")
dataset = load_dataset("deepset/prompt-injections")

# Convert the dataset to a Pandas DataFrame
df = pd.DataFrame(dataset["train"])

# Print the first few rows
print("Sample data:")
print(df.head())

# Save as CSV
csv_filename = "prompt_injections.csv"
df.to_csv(csv_filename, index=False)

print(f"Dataset successfully saved as {csv_filename}")
