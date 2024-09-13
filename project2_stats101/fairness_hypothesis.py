import matplotlib.pyplot as plt

# Data for the frequency
labels = ['No (N)', 'Yes (Y)']
maybe = [0, 47]
no = [2, 34]
yes = [1, 47]

# Fair Hypothesis Line Graph
plt.figure(figsize=(10, 6))
plt.plot(labels, maybe, marker='o', label='Maybe')
plt.plot(labels, no, marker='o', label='No')
plt.plot(labels, yes, marker='o', label='Yes')

# Adding title and labels
plt.title('Fair Hypothesis: Comfort in Discussing Mental Health with Supervisor', fontsize=14)
plt.xlabel('Mental Health Diagnosis', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Adjust the legend
plt.legend(loc='best')

# Save and display the graph
plt.tight_layout()
plt.savefig('Fairness_Hypothesis_Mental_Health_Diagnosis_Supervisor.png')
plt.show()
