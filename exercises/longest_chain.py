"""
Given a starting number:
- If it's odd, then the next value would be 3N + 1.
- If it's even, then the next value would be N/2

Eventually, it will hit 1.

Between 1 to 1,000,000 as the starting number, which number will generate the longest chain?
"""


def calculate_chain(number, count):
    if number == 1:
        return count
    elif number % 2 == 0:
        number /= 2
    else:
        number = (3 * number) + 1

    count += 1
    return calculate_chain(number, count)


longest_number = 1
longest_count = 1

for number in range(1, 1000000):
    count = calculate_chain(number, 1)

    if count > longest_count:
        longest_count = count
        longest_number = number

print longest_number, longest_count
