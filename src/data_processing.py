import pandas as pd


print("hello")
# Loads the dataset
data = pd.read_csv("data/Reviews.csv")

# First few rows to see dataset
print("Dataset Preview:")
print(data.head())

print("Missing values in each column:")
print(data.isnull().sum())