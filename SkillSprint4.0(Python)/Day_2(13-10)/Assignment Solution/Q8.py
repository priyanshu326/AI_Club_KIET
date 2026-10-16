'''8 — Set algebra: Find the common values of {1, 2, 3, 4} and {3, 4, 5, 6}. Then print their union and difference. '''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. Common values (Intersection)
print("Common values:", set1 & set2)

# 2. Union
print("Union:", set1 | set2)

# 3. Difference (set1 minus set2)
print("Difference (set1 - set2):", set1 - set2)