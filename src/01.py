from pprint import pprint
from itertools import starmap
from collections import Counter

#INP_PATH = 'test/01'
INP_PATH = 'input/01'

# read input as two lists (left and right)
with open(INP_PATH) as file:
    inp = [list(z) for z in zip(*[map(int, l.split()) for l in file.readlines()])]

# calculate the differences between the sorted elements of list 1 and list 2
def distance(left: list, right: list) -> int:
    # distance = absolute difference between pairs
    return sum(starmap(lambda a,b: abs(a - b), zip(sorted(left), sorted(right))))

# part 1 answer
pprint(distance(*inp))

# calculate the similarity between the left and the right list
def similarity(left: list, right: list) -> int:
    # use Counter object to create a map with (item, #occurrence) for the right list
    occurrence = Counter(right)
    # similarity = left item times number of occrrences in the right list
    return sum(i * occurrence[i] for i in left)

# part 2 answer
pprint(similarity(*inp))