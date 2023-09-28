pip install pandas matplotlib scikit-learn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data
target = iris.target
df = pd.DataFrame(data, columns=iris.feature_names)
df['target'] = target
# Display the first few rows of the dataset
print(df.head())

# Get summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Scatter plot of Sepal Length vs Sepal Width
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['target'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Scatter plot of Petal Length vs Petal Width
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=df['target'])
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Petal Width')
plt.show()
plt.savefig('sepal_length_vs_sepal_width.png')
plt.savefig('petal_length_vs_petal_width.png')
python data_visualization.py
