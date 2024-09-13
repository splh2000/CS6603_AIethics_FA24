import numpy as np
import matplotlib.pyplot as plt

# Data for the frequency
labels = ['No (N)', 'Yes (Y)']
maybe = [0, 47]
no = [2, 34]
yes = [1, 47]

x = np.arange(len(labels))  # label locations
width = 0.3  # bar width

# Bias Hypothesis Stacked Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(x - width, maybe, width, label='Maybe')
plt.bar(x, no, width, label='No')
plt.bar(x + width, yes, width, label='Yes')

# Adding title and labels
plt.title('Bias Hypothesis: Comfort in Discussing Mental Health with Supervisor', fontsize=14)
plt.xlabel('Mental Health Diagnosis', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Set x-ticks and legend
plt.xticks(x, labels)
plt.legend(loc='best')

# Save and display the graph
plt.tight_layout()
plt.savefig('Bias_Hypothesis_Mental_Health_Diagnosis_Supervisor.png')
plt.show()
