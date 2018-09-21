import sys

"""
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

https://leetcode.com/problems/valid-sudoku/description/
"""

initial_sudoku_board = [5, 3, '.', '.', 7, '.', '.', '.', '.',
                        6, '.', '.', 1, 9, 5, '.', '.', '.',
                        '.', 9, 8, '.', '.', '.', '.', 6, '.',
                        8, '.', '.', '.', 6, '.', '.', '.', 3,
                        4, '.', '.', 8, '.', 3, '.', '.', 1,
                        7, '.', '.', '.', 2, '.', '.', '.', 6,
                        '.', 6, '.', '.', '.', '.', 2, 8, '.',
                        '.', '.', '.', 4, 1, 9, '.', '.', 5,
                        '.', '.', '.', '.', 8, '.', '.', 7, 9]


def print_lines(symbol):
    for _ in range(21):
        print symbol,

    print ""


def print_board():
    print_lines("=")

    for row in range(0, 9):
        print "||",

        for column in range(0, 9):
            item = initial_sudoku_board[column + (row * 9)]
            item = 0 if item == '.' else item
            print str(item),

            if column in (2, 5, 8):
                print str("||"),
            else:
                print "|",
        print ""

        if row in (2, 5, 8):
            print_lines("=")
        else:
            print_lines("-")
    print


# Does a check against a set before adding
def add_number(number, number_set):
    if number in number_set:
        print "Current set: {}".format(number_set)
        print "Number to add: {}".format(number)
        print "ERROR!  Not a valid sudoku"
        sys.exit(1)
    elif number == '.':  # Ignoring zeroes
        pass
    else:
        number_set.add(number)


# Code starts here
boxes = []
rows = []
columns = []
print_board()

# Iterate through the input and add numbers in the appropriate rows, columns, boxes
for row_index in range(9):
    
    for column_index in range(9):
        item = initial_sudoku_board[column_index + (row_index * 9)]

        # Instantiate rows, boxes, columns
        if row_index == 0:
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        add_number(item, rows[row_index])
        add_number(item, columns[column_index])

        if row_index < 3 and column_index < 3:
            add_number(item, boxes[0])
        elif row_index < 3 and 2 < column_index < 6:
            add_number(item, boxes[1])
        elif row_index < 3 and 5 < column_index < 9:
            add_number(item, boxes[2])
        elif 2 < row_index < 6 and column_index < 3:
            add_number(item, boxes[3])
        elif 2 < row_index < 6 and 2 < column_index < 6:
            add_number(item, boxes[4])
        elif 2 < row_index < 6 and 5 < column_index < 9:
            add_number(item, boxes[5])
        elif row_index > 5 and column_index < 3:
            add_number(item, boxes[6])
        elif row_index > 5 and 2 < column_index < 6:
            add_number(item, boxes[7])
        elif row_index > 5 and 5 < column_index < 9:
            add_number(item, boxes[8])

print "This is a valid puzzle"
