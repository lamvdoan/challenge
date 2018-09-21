def return_longest_even_length_word():
    sentence = raw_input("Enter a sentence: ")

    # Constraint of length
    if not (1 <= len(sentence) <= 100000):
        print "Length of sentence does not meet minimum.. Length = {}".format(len(sentence))
        return

    sentence_list = sentence.split()
    longest_word = ""

    # Find the longest even length word
    for word in sentence_list:
        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word

    return "00" if longest_word == "" else longest_word

print return_longest_even_length_word()
