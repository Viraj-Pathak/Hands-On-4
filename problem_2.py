# -*- coding: utf-8 -*-
"""Problem-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rxlpPkQNdPdLYzyNHKAbFS5QMkmpi_u9
"""

def viraj_remove_duplicates(array):
    if len(array) == 0:
        return []

    # Index to store the unique elements
    unique_index = 0

    # Traverse through the array
    for i in range(1, len(array)):
        # If current element is different from previous
        if array[i] != array[unique_index]:
            unique_index += 1
            array[unique_index] = array[i]

    # Slice the array to keep only unique elements
    return array[:unique_index + 1]

# Test cases
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print("Input:")
print("array1 =", array1)
print("array2 =", array2)

output1 = viraj_remove_duplicates(array1)
output2 = viraj_remove_duplicates(array2)

print("\nOutput:")
print("array1 =", output1)
print("array2 =", output2)