import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('your_file.csv')  # Replace 'your_file.csv' with your actual file path

# Define the conditions for filtering
# Example conditions:
# Condition 1: Column 'Age' should be greater than 25
# Condition 2: Column 'Status' should be 'Active'
condition = (df['Age'] > 25) & (df['Status'] == 'Active')

# Filter the DataFrame based on the conditions
filtered_df = df[condition]

# Select the first column from the filtered DataFrame
# Assuming the first column is named 'ID', replace with actual column name if different
first_column_filtered = filtered_df.iloc[:, 0]

# Output the result
print(first_column_filtered)

# Optionally, save the filtered column to a new file
first_column_filtered.to_csv('filtered_output.csv', index=False)
