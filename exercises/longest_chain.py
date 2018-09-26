"""
Given a starting number:
- If it's odd, then the next value would be 3N + 1.
- If it's even, then the next value would be N/2

Eventually, it will hit 1.

Between 1 to 1,000,000 as the starting number, which number will generate the longest chain?
"""


class Chain:
    def __init__(self):
        pass

    count = 0

    def calculate_chain(self, number, count):
        if number == 1:
            self.count = count

        elif number % 2 == 0:
            count += 1
            number /= 2
            self.calculate_chain(number, count)

        else:
            count += 1
            number = (3 * number) + 1
            self.calculate_chain(number, count)


if __name__ == '__main__':
    longest_number = 1
    longest_count = 0

    for number in range(1, 1000000):
        count = 0

        chain = Chain()
        chain.calculate_chain(number, count)

        if chain.count > longest_count:
            longest_count = chain.count
            longest_number = number

        print number, chain.count

    print
    print "Longest Number, Longest Count"
    print longest_number, longest_count
