import pandas as pd
import matplotlib.pyplot as plt
import textwrap

# Load the dataset
df = pd.read_csv('mental-health-in-tech-survey-2019.csv')

# Select the protected class (independent variable) and dependent variable
independent_var = 'Have you ever been *diagnosed* with a mental health disorder?'
dependent_var = 'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?'

# Create a crosstab (frequency table) to analyze the relationship between the variables
fair_table = pd.crosstab(df[independent_var], df[dependent_var])

# Plot the graph for the Fair Hypothesis
plt.figure(figsize=(12, 7))
ax = fair_table.plot(kind='line', marker='o', ax=plt.gca())

title = 'Fair Hypothesis: Discussing Mental Health by Diagnosed with Mental Health Disorder'
wrapped_title = '\n'.join(textwrap.wrap(title, width=60))  # Wrap title to 60 characters per line
plt.xlabel('Mental Health Diagnosis', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# plt.legend(title=dependent_var, bbox_to_anchor=(1.05, 1), loc='upper left')
# Modify legend to show only the first 10 characters of each label
handles, labels = ax.get_legend_handles_labels()
labels = [label[:50] for label in labels]  # Limit to first 10 characters
plt.legend(handles, labels, title=dependent_var, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=3)

plt.tight_layout(rect=[0, 0.1, 1, 0.9])  
# Adjust the rectangle to make space for the legend

# plt.subplots_adjust(left=0.1, right=0.8, top=0.85, bottom=0.15)

# Save and display the graph
plt.savefig('Fair_Hypothesis_Mental_Health_Gender.png')
plt.show()
plt.close()
