"""
Create a binary tree.  Greater number goes right, otherwise go left.

Sample:
[15, 1, 30, 25, 31, 17, 16]

         15
        /  \
       1   30
           /\
         25 31
        /
       17
      /
     16

"""

import sys


class Leaf:
    number = None
    left = None
    right = None

    def __init__(self):
        pass

    def add_number(self, input_number):
        self._traverse_down_the_tree(input_number, self)

    def _traverse_down_the_tree(self, input_number, node):
        """
        Sets the number if the current node is empty.  Otherwise, figure out if it belongs on the left or right node, or
        if it needs to traverse downwards until it find an empty node to set it to.

        :param input_number: number to add
        :param node: the current node the pointer is at
        """

        if node.number is None:
            print "Setting number = {}".format(input_number)
            print
            node.number = input_number
        elif input_number > node.get_number():
            if node.right is None:
                # Create a right node since it's empty
                print "{} is Right of {}".format(input_number, node.get_number())
                node.right = Leaf()
                node.right.add_number(input_number)
            else:
                # This node has a value, traverse down the node and compare values
                self._traverse_down_the_tree(input_number, node.right)
        else:
            if node.left is None:
                # Create a left node since it's empty
                print "{} is Left of {}".format(input_number, node.get_number())
                node.left = Leaf()
                node.left.add_number(input_number)
            else:
                # This node has a value, traverse down the node and compare values
                self._traverse_down_the_tree(input_number, node.left)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_number(self):
        return self.number


class BinaryTree:
    leaf = None
    numbers = None

    def __init__(self, numbers):
        self.numbers = numbers
        self.leaf = Leaf()

        for index in range(len(self.numbers)):
            number = self.numbers[index]
            self._check_if_input_is_a_number(number)
            self.leaf.add_number(number)

    @staticmethod
    def _check_if_input_is_a_number(input_number):
        if not isinstance(input_number, int):
            print "This is not a number: {}".format(input_number)
            sys.exit(1)

    def print_tree(self):
        """
        Obsolete method, since the logging on creation was implemented after this method.  This method looks too good
        to delete, leaving it here for fun.  It also serves as a double check of the tree.

        Print the all of the vales of the tree while indicating if it's left or the right.
        """

        print "**********************************"
        print "List of numbers: "
        print self.numbers
        print
        print "Print Tree"
        print "**********"

        if self.leaf is not None:
            current_node = self.leaf
            self._print_value_of_node(current_node)
        else:
            print "No numbers"
            sys.exit(1)

    def _print_value_of_node(self, current_node):
        """
        This method prints the value of each node as it traverses downwards.
        """

        if current_node is not None:
            current_number = current_node.get_number()
            left_node = current_node.get_left()
            right_node = current_node.get_right()
            print current_number

            if left_node is not None:
                print "Check LEFT"
                print
                self._print_value_of_node(left_node)
            else:
                print "Current node [{}] has no left node:".format(current_number)

            if right_node is not None:
                print "Check RIGHT"
                print
                self._print_value_of_node(right_node)
            else:
                print "Current node [{}] has no right node:".format(current_number)

sample_numbers = [15, 1, 30, 25, 31, 17, 16]
binary_tree = BinaryTree(sample_numbers)
binary_tree.print_tree()
