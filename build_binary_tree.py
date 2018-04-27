import sys


class Tree:
    number = None
    left = None
    right = None

    def __init__(self):
        pass

    # TODO: Traverse thru the tree
    def add_number(self, input_number):
        if not isinstance(input_number, int):
            print "This is not a number: {}".format(input_number)
            sys.exit(1)

        if self.number is None:
            print "Setting number = {}".format(input_number)
            print
            self.number = input_number
        elif input_number > self.get_number():
            if self.left is None:
                print "Creating Left: {} <= {}".format(input_number, self.get_number())
                self.left = Tree()
                self.left.add_number(input_number)
            else:
                self._get_node(self.left)
        else:

        # if self.number is None:
        #     print "Setting number = {}".format(input_number)
        #     print
        #     self.number = input_number
        # elif input_number > self.get_number():
        #     print "Creating Right: {} > {}".format(input_number, self.get_number())
        #     self.right = Tree()
        #     self.right.add_number(input_number)
        # else:
        #     print "Creating Left: {} <= {}".format(input_number, self.get_number())
        #     self.left = Tree()
        #     self.left.add_number(input_number)

    def _get_node(self, current_node):


    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_number(self):
        return self.number


class BinaryTree:
    main_tree = None

    def __init__(self):
        pass

    def create_tree(self, numbers):
        self.main_tree = Tree()

        for index in range(len(numbers)):
            number = numbers[index]
            self.main_tree.add_number(number)

    def print_tree(self):
        print
        print "Print Tree"
        print "**********************"
        if self.main_tree is not None:
            current_node = self.main_tree
            self._print_value_of_node(current_node)
        else:
            print "No numbers"
            sys.exit(1)

    def _print_value_of_node(self, current_node):
        print "_get_value_of_node()"
        if current_node is not None:
            print str(current_node.get_number()) + ", "

            if current_node.get_left() is not None:
                print "Check LEFT"
                self._print_value_of_node(current_node.get_left())
            elif current_node.get_right() is not None:
                print "Check RIGHT"
                self._print_value_of_node(current_node.get_right())

            if current_node.get_right() is not None:
                print "Check RIGHT"
                self._print_value_of_node(current_node.get_right())
            elif current_node.get_left() is not None:
                print "Check LEFT"
                self._print_value_of_node(current_node.get_left())


# numbers = [10, 12, 9]
numbers = [10, 12, 9, 13, 7, 8]
binary_tree = BinaryTree()
binary_tree.create_tree(numbers)

print numbers
binary_tree.print_tree()
