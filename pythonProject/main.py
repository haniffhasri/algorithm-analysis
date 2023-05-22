# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pandas as pd

current_dir = os.getcwd()
print("Current Working Directory: ", current_dir)

# Load the CSV file into a pandas dataframe
data = pd.read_csv("sales_data.csv")

# Display the first 5 rows of the dataframe
print(data.head(10))

# Check the dimensions of the dataframe
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

# Check for missing values in the dataframe
print("Number of missing values:", data.isnull().sum().sum())

# Compute summary statistics of the dataframe
summary = data.describe()
print(summary)
print(data.columns)
# Visualize the distribution of a variable using a histogram
import matplotlib.pyplot as plt

# data["Profit"].hist(bins=10)
plt.hist(data["Revenue"], bins=100)
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# Perform data cleaning and transformation
data = data.dropna()  # Remove rows with missing values
data["Profit"] = data["Revenue"] - data["Cost"]  # Compute the profit

# Perform a basic machine learning task using scikit-learn
from sklearn.linear_model import LinearRegression

X = data[["Revenue", "Cost"]]  # Independent variables
y = data["Profit"]  # Dependent variable

model = LinearRegression()
model.fit(X, y)

# Create a scatter plot of the data points
plt.scatter(X["Revenue"], y, color='blue', label="Revenue")
plt.scatter(X["Cost"], y, color='green', label="Cost")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
plt.legend()

# Overlay the predicted values from the model as a line plot
x_values = pd.DataFrame(
    {'Revenue': [X["Revenue"].min(), X["Revenue"].max()], 'Cost': [X["Cost"].min(), X["Cost"].max()]})
y_values = model.predict(x_values)
plt.plot(x_values["Revenue"], y_values, color='red', linewidth=2)
plt.plot(x_values["Cost"], y_values, color='orange', linewidth=2)

# Show the plot
plt.show()
