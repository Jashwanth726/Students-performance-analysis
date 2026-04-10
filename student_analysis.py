import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('student_performance_sample.csv')

# Calculate correlation (selecting only numeric columns to avoid errors)
correlation_matrix = df.select_dtypes(include=['number']).corr()

# Create Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn') # Fixed 'RdY1Gn' to 'RdYlGn'
plt.title('Correlation Heatmap of Academic Factors')

# Save the plot locally so you can upload the image to GitHub too
plt.savefig('heatmap.png')
plt.show()