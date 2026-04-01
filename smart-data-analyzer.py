import pandas as pd

# Load dataset
df = pd.read_csv("student-data.csv")

# It will Print the Dataset Overview Total Rows,Total Column
print("--- DATASET OVERVIEW ---") 
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# It will print the all the columns into the list form
print("\n--- COLUMN NAMES ---")
print(df.columns.to_list)

# It will print the all of the columns names and its data types
print("\n--- DATA TYPES ---")
print(df.dtypes)  

# It will print the all of the columns names with the sum of null values in each column.
print("\n---Missing Values----")
print(df.isnull().sum())

# It will print the  0 to 4 rows and columns data 
print("\n--- First 5 Rows---")
print(df.head())

