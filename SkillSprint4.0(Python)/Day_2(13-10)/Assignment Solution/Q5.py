'''5 — Tuple access: Given colours = ("red", "green", "blue"), print the last item and a slice. Then try changing the first item and observe what happens.'''

colours = ("red", "green", "blue")

print("Last item:", colours[-1])

print("Slice:", colours[:2])

colours[0] = "yellow" #TypeError: 'tuple' object does not support item assignment

