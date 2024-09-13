import pandas as pd
import matplotlib.pyplot as plt
import re

# Load the dataset
df = pd.read_csv('mental-health-in-tech-survey-2019.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(f"Number of Observations: {df.shape[0]}")
print(f"Number of Variables: {df.shape[1]}")
print("\n")

# Print all variable (column) names
column_names = df.columns

# print("Variable (Column) names in the dataset:")
# for col in column_names:
#     print(col)

# Select the protected class variables (independent variables)
independent_vars = ['Do you have a family history of mental illness?',
                    'What is your race?', 
                    'Have you ever been *diagnosed* with a mental health disorder?']

# Select the dependent variables
dependent_vars = ['Have you ever sought treatment for a mental health disorder from a mental health professional?',
                  'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?',
                  ]

# Function to sanitize file names by removing invalid characters
def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)

# Frequency table and histogram for each dependent variable against each independent variable
for dep_var in dependent_vars:
    for ind_var in independent_vars:
        print(f"\nFrequency table for Dependent Variable: {dep_var} vs Independent Variable: {ind_var}")
        frequency_table = pd.crosstab(df[ind_var], df[dep_var])

        print(frequency_table)

         # Increase figure size to handle long titles
        plt.figure(figsize=(12, 7))

        # Plotting histograms
        frequency_table.plot(kind='bar', stacked=True, ax=plt.gca())

        # plt.title(f"Frequency of {dep_var} by {ind_var}")
        title_text = f"Frequency of {dep_var} by {ind_var}"
        if len(title_text) > 50:
            title_text = '\n'.join([title_text[i:i+50] for i in range(0, len(title_text), 50)])
        
        plt.title(title_text)
        plt.xlabel(ind_var, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # plt.savefig('Figure1.png')
        file_name = sanitize_filename(f"{dep_var}_vs_{ind_var}.png")
        plt.savefig(file_name)
        plt.show()
        plt.close()

# # Check for missing values
# print("Missing Values Information:")
# missing_values = df.isnull().sum()
# print(missing_values[missing_values > 0])

# # Drop columns with more than 50% missing values
# df_cleaned = df.dropna(thresh=len(df) * 0.5, axis=1)

# # Fill missing values in the remaining columns with suitable methods (e.g., mode for categorical, mean for numerical)
# for column in df_cleaned:
#     if df_cleaned[column].dtype == 'object':
#         df_cleaned[column].fillna(df_cleaned[column].mode()[0], inplace=True)
#     else:
#         df_cleaned[column].fillna(df_cleaned[column].mean(), inplace=True)

# # Export the cleaned data to a new CSV file
# output_path = "cleaned_mental_health_survey.csv"
# df_cleaned.to_csv(output_path, index=False)
# print(f"Cleaned dataset has been saved to {output_path}")
