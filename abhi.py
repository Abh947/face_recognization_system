import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Scatter plot
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'], hue=iris.target_names[df['species']])
plt.title('Scatter plot: Sepal Length vs Sepal Width')
plt.show()
