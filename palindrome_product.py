"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 99.  Find the largest palindrome made from the product of two 3-digit numbers.

Disclaimer: I originally did not come up with optimal idea to solve this quicker.  I incremented the for loop instead.
"""

from datetime import datetime
import sys


def get_max_palindrome_product():
    # Input constraint check
    number_of_digits = raw_input("Enter number of digits (1-6): \n")

    start_time = datetime.utcnow()

    try:
        number_of_digits = int(number_of_digits)
    except ValueError:
        print "Invalid input: {}".format(number_of_digits)
        sys.exit()

    if number_of_digits < 1 or number_of_digits > 6:
        print "Invalid digits: {}".format(number_of_digits)
        sys.exit()

    # Initialize variables
    max_number = get_max_number(number_of_digits)
    min_number = get_min_number(number_of_digits)

    max_palindrome = 0
    multiplicand = 0
    multiplier = 0

    # Get palindrome
    for outer in range(max_number, min_number, -1):
        for inner in range(max_number, min_number, -1):
            product = outer * inner

            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product
                multiplicand = outer
                multiplier = inner

                # If the absolute max is found during a change of outer, then no need to iterate
                break

        # if the max product of the remaining numbers to iterate is less than the max palindrome, then no need to iterate
        if outer * 999 < max_palindrome:
            break

    print "Outer number: {}".format(multiplicand)
    print "Inner number: {}".format(multiplier)
    print "Max palindrome: {}\n".format(max_palindrome)

    time_elapsed = (datetime.utcnow() - start_time).total_seconds()
    print "Total seconds: {}".format(time_elapsed)


def get_max_number(number_of_digits):
    max_number = ""
    for number in range(0, number_of_digits):
        max_number += "9"
    return int(max_number)


def get_min_number(number_of_digits):
    min_number = "1"
    for number in range(0, number_of_digits - 1):
        min_number += "0"
    return int(min_number)


def is_palindrome(number):
    number = str(number)
    return True if number == number[::-1] else False


get_max_palindrome_product()
