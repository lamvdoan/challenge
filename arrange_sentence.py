"""
Rearrange the words in the sentence according to the length of the word.
"""

import unittest


class MyTestCase(unittest.TestCase):
    def arrange(self, sentence):
        # Gracefully handle bad data
        if sentence is None:
            return None
        elif sentence == "":
            return ""

        # Append the split words into a list
        words_list = sentence.split(" ")

        # Store <key,value> of <length, word>
        words_dict = {}
        max_length = 0
        for word in words_list:
            # Get max length to iterate later
            if len(word) > max_length:
                max_length = len(word)

            # Concatenate the dupes
            if len(word) in words_dict:
                words_dict[len(word)] = words_dict[len(word)] + " " + word
            # Store the values if no dupes found
            else:
                words_dict[len(word)] = word

        # Sort the list by length
        sorted_list = []
        for i in range(0, max_length + 1):
            for key, value in words_dict.items():
                if i == key:
                    sorted_list.append(value)

        # Concatenate the words
        new_sentence = ""
        for item in sorted_list:
            new_sentence += item + " "

        # Lowercase all the letters and remove the trailing space
        new_sentence = new_sentence[:-1].lower()

        # Make the first letter upper case
        bs = bytearray(new_sentence)
        bs[0] = new_sentence[0].upper()
        return str(bs)

    # Jason's version of the solution
    def arrange_using_jasons_solution(self, sentence):
        dict_word_lists = {}
        sorted_string = ""
        list_words = sentence.replace(".", "").lower().split(" ")

        for each_word in list_words:
            dict_word_lists.setdefault(len(each_word), []).append(each_word)

        for each_len in sorted(dict_word_lists.keys()):
            sorted_string = ' '.join([sorted_string, ' '.join(dict_word_lists[each_len])])

        sorted_string = ''.join([sorted_string.strip().capitalize(), "."])

        return sorted_string

    def test_dupe_words(self):
        self.assertEqual(self.arrange("test Blah WoohoO test up"), "Up test blah test woohoo")
        self.assertEqual(self.arrange_using_jasons_solution("test Blah WoohoO test up"), "Up test blah test woohoo.")

    def test_complex_sentence(self):
        self.assertEqual(self.arrange("This is a more complicated example sentence"),
                         "A is this more example sentence complicated")
        self.assertEqual(self.arrange_using_jasons_solution("This is a more complicated example sentence"),
                         "A is this more example sentence complicated.")

    def test_one_word(self):
        self.assertEqual(self.arrange("hello"), "Hello")
        self.assertEqual(self.arrange_using_jasons_solution("hello"), "Hello.")

    def test_no_word(self):
        self.assertEqual(self.arrange(""), "")
        self.assertEqual(self.arrange_using_jasons_solution(""), ".")

    def test_no_word(self):
        self.assertIsNone(self.arrange(None))


if __name__ == '__main__':
    unittest.main()
