#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
i = 0

while i < len(array):
    if array[i] > 5:
        new_array.append(array[i]+2)
    i += 1
print(f"Original array: {array}")
print(f"New array: {new_array}")