import pandas as pd
import io # imports the io library which helps handle text/data streams

# Load the 2024 dataset
data_2024 = pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb24.csv')

# Display basic information
print("Dataset Shape:") 
print(data_2024.shape) # prints how many rows and columns are in the dataset (rows, columns)
print("\n" + "=="*40 + "\n") # separator for readability

print("Column Names & Data Types:")
buffer = io.StringIO() # creates empty string container called buffer
data_2024.info(buf=buffer) # writes the output of data_2024.info() to the buffer instead of console
info_output = buffer.getvalue().split('\n')[1:] # splits output into lines and skips the first line
print('\n'.join(info_output)) # prints the relevant lines from the info output
print("\n" + "=="*40 + "\n") # separator for readability

print("First 5 Rows of the Dataset:")
print(data_2024.head()) # prints the first 5 rows of the dataset
print("\n" + "=="*40 + "\n") # separator for readability

print("Missing Values:")
print(data_2024.isnull().sum()) # counts and prints the number of missing values in each column
print("\n" + "=="*40 + "\n") # separator for readability

print("Basic Statistics:")
print(data_2024.describe()) # prints basic statistics for numerical columns


#Load the rest of the datasets for comparison
print("\n" + "=="*40 + "\n") # separator for readability
print("Loading additional datasets for comparison")
print("\n" + "=="*40 + "\n") # separator for readability

datasets = {
    '2020': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb20.csv'),
    '2021': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb21.csv'),
    '2022': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb22.csv'),
    '2023': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb23.csv'),
    '2024': pd.read_csv('/Users/tylerpayne/Personal/NCAA-Analytics/Dataset/cbb24.csv')
}

# Compare each dataset
for year, df in datasets.items():
    print(f"Dataset Year: {year}")
    print(f"Shape:", {df.shape})
    print(f"Column Names: {df.columns.tolist()}")
    print(f"Missing Values: {df.isnull().sum().sum()} total") # total missing values in the dataset


    print("\n" + "=="*40 + "\n") # separator for readability
    print("Identify Data Inconsistencies Across Years")
    print("\n" + "=="*40 + "\n") # separator for readability

    # Get all uniqe columns across all datasets
    all_columns = set()
    for year, df in datasets.items():
        all_columns.update(df.columns)

    print("Total unique columns across all years:", len(all_columns))
    print(f"Columns: {sorted(all_columns)}")
    print("\n")

    # Find commmon columns
    common_columns = set(datasets['2020'].columns)
    for year, df in datasets.items():
        common_columns = common_columns.intersection(df.columns)
    
    print("Common columns across all years:", len(common_columns))
    print(f"Columns: {sorted(common_columns)}")
    print("\n")

    # Find unique columns per dataset
    print("Unique columns per dataset:")
    for year, df in datasets.items():
        unique_cols = set(df.columns) - common_columns
        if unique_cols:
            print(f" {year}: {sorted(unique_cols)}")
    print("\n")