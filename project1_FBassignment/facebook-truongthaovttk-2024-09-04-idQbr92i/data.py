import pandas as pd

# Define path
html_path = 'ad_preferences.html'

# Read Table from html
tables = pd.read_html(html_path)

# Print Table, separated by empty rows
# for table in tables:
#     print(table, '\n\n')

# Concatenate all tables into one DataFrame
combined_df = pd.concat(tables, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined_tables.csv', index=False)

# Read the file, skipping the first 389 lines
data = pd.read_csv('combined_tables.csv', skiprows=389)

# Save the remaining data to a new file
data.to_csv('filtered_data.csv', index=False)