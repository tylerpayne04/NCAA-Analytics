import pandas as pd

# Load all datasets
datasets = {
    '2020': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb20.csv'),
    '2021': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb21.csv'),
    '2022': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb22.csv'),
    '2023': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb23.csv'),
    '2024': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb24.csv')
}

print("Starting data cleaning")
print("="*40 + "\n")

# Clean each dataset
for year, df in datasets.items():
    print(f"Cleaning {year} dataset...")
    
    # Drop RK column if it exists (only in 2020)
    if 'RK' in df.columns:
        df = df.drop('RK', axis=1)
        print(f"  - Dropped RK column")
    
    # Standardize column names: EFGD_D -> EFG_D
    if 'EFGD_D' in df.columns:
        df = df.rename(columns={'EFGD_D': 'EFG_D'})
        print(f"  - Renamed EFGD_D to EFG_D")
    
    # Standardize 2024 column names: EFG% -> EFG_O, EFGD% -> EFG_D
    if 'EFG%' in df.columns:
        df = df.rename(columns={'EFG%': 'EFG_O'})
        print(f"  - Renamed EFG% to EFG_O")
    
    if 'EFGD%' in df.columns:
        df = df.rename(columns={'EFGD%': 'EFG_D'})
        print(f"  - Renamed EFGD% to EFG_D")

    # Add POSTSEASON and SEED columns if they don't exist (only 2020)
    if 'POSTSEASON' not in df.columns:
        df['POSTSEASON'] = None
        print(f"  - Added POSTSEASON column with null values")
    
    if 'SEED' not in df.columns:
        df['SEED'] = None
        print(f"  - Added SEED column with null values")
    
    # Save cleaned dataset
    df.to_csv(f'/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb{year[-2:]}.csv', index=False)
    print(f"  - Saved cleaned dataset\n")

print("="*40)
print("Data cleaning completed.")