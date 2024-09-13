import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
df = pd.read_csv('mental-health-in-tech-survey-2019.csv')

# Select the protected class variable (independent variable)
protected_class_var = 'Have you ever been *diagnosed* with a mental health disorder?'

# Map categorical values to numerical values
df[protected_class_var] = df[protected_class_var].map({'Yes': 1, 'No': 0})

# Drop any rows where the variable is NaN or empty (if applicable)
df = df.dropna(subset=[protected_class_var])

# Step 1: Calculate the mean, median, and mode for the original dataset
mean_original = df[protected_class_var].mean()
median_original = df[protected_class_var].median()
mode_original = df[protected_class_var].mode()[0]  # Use pandas mode


print(f"Original Data Set (Protected Class Variable: {protected_class_var}):")
print(f"Mean: {mean_original}")
print(f"Median: {median_original}")
print(f"Mode: {mode_original}\n")

# Step 2: Perform random sampling to create a 50% reduced dataset
df_reduced = df.sample(frac=0.5, random_state=42)  
# 50% random sample with a fixed random seed

# Step 3: Calculate the mean, median, and mode for the reduced dataset
mean_reduced = df_reduced[protected_class_var].mean()
median_reduced = df_reduced[protected_class_var].median()
mode_reduced = df_reduced[protected_class_var].mode()[0]  
# Using pandas' mode function

print(f"Reduced Data Set (50% Sample):")
print(f"Mean: {mean_reduced}")
print(f"Median: {median_reduced}")
print(f"Mode: {mode_reduced}\n")

# Step 4: Check for any differences
print("Difference in Mean:", mean_original - mean_reduced)
print("Difference in Median:", median_original - median_reduced)
print("Difference in Mode:", mode_original - mode_reduced)
