"""
Given an array, the new value of each element is the product of every other elements excluding itself.
array[n] = array[min(n)] * array[n+1] * ...  * array[max(n)]

Example:
array = [1, 3, 5], then new_array = [15, 5, 3].
array[0] = array[1] * array[2] = 3 * 5 = 15
array[1] = array[0] * array[2] = 1 * 5 = 5
array[2] = array[0] * array[1] = 1 * 3 = 3

The solution for O(n^2) is to iterate over the array and then multiply all other numbers beside itself.
Do this with O(n).

Try different sets of numbers:
[1, 3, 5] -> [15, 5, 3]
[3, 0, 5] -> [0, 15, 0]
[3, 0, 0, 5] -> [0, 0, 0, 0]
"""

does_one_zero_exist = False
does_multiple_zero_exist = False
original_array = [1, 3, 5]
# original_array = [3, 0, 5]
# original_array = [3, 0, 0, 5]

# Calculate the existence of how many zeroes and the total product
total_product = 1
for index, value in enumerate(original_array):
    if value != 0:
        total_product *= value
    elif does_one_zero_exist:
        does_multiple_zero_exist = True
    else:
        does_one_zero_exist = True

# Calculate the product for each element
new_array = []
for value in original_array:
    if does_multiple_zero_exist:
        new_array.append(0)
    else:
        if does_one_zero_exist:
            if value == 0:
                new_array.append(total_product)
            else:
                new_array.append(0)
        else:
            new_array.append(total_product / value)


print original_array
print new_array
