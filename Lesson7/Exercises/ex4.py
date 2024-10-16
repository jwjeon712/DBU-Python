# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Exercise 4: generate a scatter plot between two features
# x = df['sepal length (cm)'], y = df['sepal width (cm)']
x = df['sepal length (cm)']
y = df['sepal width (cm)']

# plt.scatter(x, y) creates a scatter plot of x vs y
plt.scatter(x, y)

# plt.title() sets the title of the plot
plt.title('Scatter Plot of Sepal Length vs Sepal Width')

# plt.xlabel() sets the label for the x-axis
plt.xlabel('Sepal Length (cm)')

# plt.ylabel() sets the label for the y-axis
plt.ylabel('Sepal Width (cm)')

# plt.show() displays the plot
plt.show()





