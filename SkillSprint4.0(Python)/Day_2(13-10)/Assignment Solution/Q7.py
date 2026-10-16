'''7 — Dictionary update: Create a dictionary for a student. Add a branch key, change an existing value, print its keys and values, then delete one key. '''

# 1. Create a dictionary for a student
student = {"name": "Aman","age": 20,"grade": "A"}

# 2. Add a 'branch' key
student["branch"] = "Computer Science"

# 3. Change an existing value (e.g., update the grade)
student["grade"] = "A+"

# 4. Print its keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# 5. Delete one key (e.g., delete 'age')
del student["age"]

# Final dictionary state
print("\nFinal student dictionary:", student)