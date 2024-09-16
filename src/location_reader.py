import pandas as pd

# Specify the path to your Excel file
file_path = '../data/Missing locations.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the DataFrame
print(df)