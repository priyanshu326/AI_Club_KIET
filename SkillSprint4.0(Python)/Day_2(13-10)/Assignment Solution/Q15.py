'''15 — Loop choice: Print the items of a list using both a for loop and a while loop. '''

fruits = ["apple", "banana", "cherry"]

print("--- Using For Loop ---")
for fruit in fruits:
    print(fruit)

print("\n--- Using While Loop ---")
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
