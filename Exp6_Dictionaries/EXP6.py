# dictionaries
emp = {
    "E101": 45000,
    "E102": 52000,
    "E103": 48000,
    "E104": 33000,
    "E105": 22000,
    "E106": 46000
}
print("\nOriginal Dictionary:", emp)

#keys
print("Employee IDs:", emp.keys())

#values
print("Salaries:", emp.values())

#copy
emp_copy = emp.copy()
print("Copied Dictionary:", emp_copy)

#update
emp.update({"E107": 40000})
print("After Update:", emp)

#pop
emp.pop("E105")
print("After Pop:", emp)

#delete
del emp["E104"]
print("After Delete:", emp)

# final dictionary
print("Final Dictionary:", emp)