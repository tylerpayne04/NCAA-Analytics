import pandas as pd

print("Loading all datasets")
print("="*40 + "\n")

# Load all cleaned datasets
datasets = {
    '2020': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb20.csv'),
    '2021': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb21.csv'),
    '2022': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb22.csv'),
    '2023': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb23.csv'),
    '2024': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb24.csv')
}

# Combine datasets into a single DataFrame
combined_df = pd.concat(datasets.values(), ignore_index=True)

print(f"Combined dataset shape: {combined_df.shape}")
print(f"Total rows: {combined_df.shape[0]}")
print(f"Total columns: {combined_df.shape[1]}")
print("\n" + "="*40 + "\n")

print("Sample of combined dataset:")
print(combined_df.head(10))
print("\n" + "="*40 + "\n")

print("Missing Values in Combined Dataset:")
print(combined_df.isnull().sum())
print("\n" + "="*40 + "\n")

#Save combined dataset
combined_df.to_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/combined_cbb_data.csv', index=False)
print("Combined dataset saved to 'combined_cbb_data.csv'")