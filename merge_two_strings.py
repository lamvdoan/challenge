import unittest

"""
Merge two strings together e.g. abc and xyz would be axbycz
"""


class MyTestCase(unittest.TestCase):
    def merge_strings(self, string_one, string_two):

        length_string_one = len(string_one)
        length_string_two = len(string_two)

        if not ((1 <= length_string_one <= 25000) and (1 <= length_string_two <= 25000)):
            return None

        max_iter = length_string_one if length_string_one > length_string_two else length_string_two

        merging_string = ""

        for i in range(0, max_iter):
            if i <= length_string_one - 1:
                merging_string += string_one[i]

            if i <= length_string_two - 1:
                merging_string += string_two[i]

        return merging_string

    def test_differ_length(self):
        self.assertEqual(self.merge_strings('abc', 'defghi'), 'adbecfghi')

    def test_same_length(self):
        self.assertEqual(self.merge_strings('abc', 'def'), 'adbecf')

    def test_long_length(self):
        long_string = ""

        for i in range(0, 25001):
            long_string += "a"

        self.assertIsNone(self.merge_strings('', long_string))

    def test_zero_length(self):
        self.assertIsNone(self.merge_strings('', 'asdf'))


if __name__ == '__main__':
    unittest.main()
