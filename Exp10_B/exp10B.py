import matplotlib.pyplot as plt
import numpy as np

#1. line plot
x = np.arange(0, 10, 1)
y = x ** 2

plt.plot(x, y, color="blue", marker="o")
plt.title("Matplotlib Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#2. bar chart

categories = ["A", "B", "C"]
values = [10, 20, 15]

plt.bar(categories, values, color=["red", "green", "blue"])
plt.title("Matplotlib Bar Chart")
plt.show()


#3. histogram
data = np.random.randn(1000)

plt.hist(data, bins=20, color="purple", edgecolor="black")
plt.title("Matplotlib Histogram")
plt.show()


#4. scatter plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color="orange")
plt.title("Matplotlib Scatter Plot")
plt.show()




