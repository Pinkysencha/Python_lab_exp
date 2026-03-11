# List for student marks
marks = [75, 80, 65, 90]
print("Original Marks:", marks)

# append
marks.append(85)
print("After append:", marks)

# insert
marks.insert(2, 70)
print("After insert:", marks)

#extend
marks.extend([88, 92])
print("After extend:", marks)

#copy
marks_copy = marks.copy()
print("Copied Marks:", marks_copy)

#print
print("Student Marks:")
for m in marks:
    print(m)

#clear
print("After using clear:", marks)