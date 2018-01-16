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


def print_them():
    print box0
    print box1
    print box2
    print box3
    print box4
    print box5
    print box6
    print box7
    print box8
    print

    print row0
    print row1
    print row2
    print row3
    print row4
    print row5
    print row6
    print row7
    print row8
    print

    print column0
    print column1
    print column2
    print column3
    print column4
    print column5
    print column6
    print column7
    print column8


# Code starts here

box0 = set()
box1 = set()
box2 = set()
box3 = set()
box4 = set()
box5 = set()
box6 = set()
box7 = set()
box8 = set()

row0 = set()
row1 = set()
row2 = set()
row3 = set()
row4 = set()
row5 = set()
row6 = set()
row7 = set()
row8 = set()

column0 = set()
column1 = set()
column2 = set()
column3 = set()
column4 = set()
column5 = set()
column6 = set()
column7 = set()
column8 = set()

print_board()

# Iterate through the input and add numbers in the appropriate rows, columns, boxes
for row in range(9):
    for column in range(9):
        item = initial_sudoku_board[column + (row * 9)]

        if row == 0:
            add_number(item, row0)
        elif row == 1:
            add_number(item, row1)
        elif row == 2:
            add_number(item, row2)
        elif row == 3:
            add_number(item, row3)
        elif row == 4:
            add_number(item, row4)
        elif row == 5:
            add_number(item, row5)
        elif row == 6:
            add_number(item, row6)
        elif row == 7:
            add_number(item, row7)
        elif row == 8:
            add_number(item, row8)

        if column == 0:
            add_number(item, column0)
        elif column == 1:
            add_number(item, column1)
        elif column == 2:
            add_number(item, column2)
        elif column == 3:
            add_number(item, column3)
        elif column == 4:
            add_number(item, column4)
        elif column == 5:
            add_number(item, column5)
        elif column == 6:
            add_number(item, column6)
        elif column == 7:
            add_number(item, column7)
        elif column == 8:
            add_number(item, column8)

        if row < 3 and column < 3:
            add_number(item, box0)
        elif row < 3 and 2 < column < 6:
            add_number(item, box1)
        elif row < 3 and 5 < column < 9:
            add_number(item, box2)
        elif 2 < row < 6 and column < 3:
            add_number(item, box3)
        elif 2 < row < 6 and 2 < column < 6:
            add_number(item, box4)
        elif 2 < row < 6 and 5 < column < 9:
            add_number(item, box5)
        elif row > 5 and column < 3:
            add_number(item, box6)
        elif row > 5 and 2 < column < 6:
            add_number(item, box7)
        elif row > 5 and 5 < column < 9:
            add_number(item, box8)

print "This is a valid puzzle"
