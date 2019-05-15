"""
Given a list of pair of words, see if there is a match for both words in a
list of sentences.  It has to be an exact match of the word.  Ignore match
if the word is an empty string.

Example:
Sentence: the lazy brown fox jumped over the fat dog
------------------
[lazy, fox]: True
[jumped, ov]: False
[jumped, over]: True
[, fat]: True
[nonexistent, ]: False

The solution below uses data frames to make life more difficult.
"""

import pandas as pd

############ SET UP ###############
data_words = {
    'one': ['lazy', 'jumped', 'jumped', '', 'nonexistent'],
    'two': ['fox', 'ov', 'over', 'fat', '']
}

data_notes = {
    "a": ["the lazy brown fox jumped over the fat dog", "some new sentences"]
}

df_words = pd.DataFrame(data_words, columns=['one', 'two', 'category'])
df_notes = pd.DataFrame(data_notes, columns=['a'])

list_of_notes = []

############ ALGORITHM ##################

# Get list of notes
for row in df_notes.itertuples():
    list_of_notes.append(row.a)

# NOTE: O notation is n^3.  That's very bad lol.

# Iterate over each note
for note in list_of_notes:
    notes = note.split()

    print 'Sentence: {}'.format(note)
    print '------------------'

    # Iterate over each pair of words
    for row in df_words.itertuples():
        does_word_one_match = False
        does_word_two_match = False

        # Compare each pair of words against each word in the note
        for word in notes:

            # Check match for word one
            if row.one != '':
                if word == row.one:
                    does_word_one_match = True
            else:
                does_word_one_match = True

            # Check match for word two
            if row.two != '':
                if word == row.two:
                    does_word_two_match = True
            else:
                does_word_one_match = True

            # Skip checking if there's a match for both words
            if does_word_one_match and does_word_two_match:
                break

        does_all_words_exist = does_word_one_match and does_word_two_match
        print '[{}, {}]: {}'.format(row.one, row.two, does_all_words_exist)

    print
