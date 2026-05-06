# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
    
# Load dataset
data = pd.read_csv("Statistics_activity_2.xlsx")   # replace with your file name

# Explore data
print("First 5 rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Clean data
data = data.dropna()            # remove missing values
data = data.drop_duplicates()  # remove duplicate rows

# Select variables
x = data.iloc[:, 0]   # first column
y = data.iloc[:, 1]   # second column

# --------- Visualizations ---------

# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Histogram
plt.figure()
plt.hist(x)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()