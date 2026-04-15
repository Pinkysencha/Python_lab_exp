import numpy as np
import pandas as pd

# NumPy Example
print(" NumPy Operations")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))

# Pandas
print("\npandas Operation")

data = {
    "Flowers": ["Rose", "Lily", "Tulip", "Jasmine", "Lotus", "Sunflower", "Daisy", "Orchid", "Lavender", "Marigold"],
    "Fruits": ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Cherry", "Papaya", "Guava", "Watermelon"],
    "Toothpaste": ["Colgate", "Closeup", "Pepsodent", "Sensodyne", "Colgate", "Closeup", "Pepsodent", "Sensodyne", "Colgate", "Closeup"],
    "Crackers": ["Lays", "Kurkure", "Bingo", "Pringles", "Lays", "Kurkure", "Bingo", "Pringles", "Lays", "Kurkure"],
    "Games": ["Chess", "Cricket", "Football", "Tennis", "Hockey", "Badminton", "Kabaddi", "Carrom", "Ludo", "Baseball"],
    "Marks": [85, 90, 78, 88, 92, 76, 81, 95, 89, 84],
    "Age": [20, 21, 19, 22, 20, 23, 21, 20, 22, 19],
    "Height": [160, 165, 170, 155, 168, 172, 158, 166, 169, 162],
    "Weight": [55, 60, 65, 50, 58, 70, 52, 61, 63, 57],
    "City": ["Chennai", "Delhi", "Mumbai", "Kolkata", "Bangalore", "Hyderabad", "Pune", "Jaipur", "Goa", "Coimbatore"]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

