#!/usr/bin/env python3
from ordered_set import OrderedSet

array = [2, 8, 9, 48, 8, 22, -12, 2]
# new_array = [x+2 for x in array if x>5]

new_array = []

for i in range(len(array)):
    if array[i-1] not in array[:i-1]: # same as [0:i-1], meaning from index 0 until i-1
        if array[i-1] > 5:
            new_array.append(array[i-1]+2)

#i = 0
#while i < len(array):
#    if array[i] > 5:
#        new_array.append(array[i]+2)
#    i += 1

new_set = OrderedSet(new_array)
print(f"Original array: {array}")
print(f"New array: {new_set}")