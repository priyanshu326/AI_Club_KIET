'''2 — List operations: Start with [10, 20, 30]. Replace the middle value, append 40, and extend the list with [50, 60].'''

lst = [10, 20, 30]
new_value = 25
lst[1] = new_value
lst.append(40)
lst.extend([50, 60])
print("Final list:", lst)