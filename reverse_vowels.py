"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

O notation = N + <occurrence of vowels>
"""

from datetime import datetime


def reverse_vowels_of_string():
    original_string = raw_input("Enter a string: ")

    # Starting timer
    start_time = datetime.utcnow()

    # Initialize variables
    reversed_string = list(original_string)
    list_of_vowels = []
    list_of_indices = []

    # Gather a list of vowels and a list of their indices
    for index in range(0, len(original_string) - 1):
        if is_a_vowel(original_string[index]):
            list_of_vowels.append(original_string[index])
            list_of_indices.append(index)

    # Iterate over indices in ascending order and pop the last vowel
    for index in list_of_indices:
        reversed_string[index] = list_of_vowels.pop()

    print "\nOriginal String: {}".format(original_string)
    print "Reversed String: {}\n".format(''.join(reversed_string))

    # Ending timer
    time_elapsed = (datetime.utcnow() - start_time).total_seconds()
    print "Total seconds: {}".format(time_elapsed)


def is_a_vowel(char):
    vowels = {"a", "e", "i", "o", "u"}

    for vowel in vowels:
        if char == vowel:
            return True

    return False


reverse_vowels_of_string()
