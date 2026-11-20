
from datasets import load_dataset
import pandas as pd

print("Loading MATH algebra dataset...")

dataset = load_dataset(
    "EleutherAI/hendrycks_math",
    "algebra"
)

print("\nDataset loaded successfully!")

# Display dataset sizes
for split in dataset:
    print(f"{split}: {len(dataset[split])} problems")

# Display sample problems
df = pd.DataFrame(dataset["train"])

print("\nDataset columns:")
print(df.columns.tolist())

print("\nDifficulty distribution:")
print(df["level"].value_counts())

print("\nExample problem:")
print(df.iloc[0]["problem"])

print("\nExample solution:")
print(df.iloc[0]["solution"][:500])

print("\nDataset exploration complete!")
