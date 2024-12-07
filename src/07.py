from pprint import pprint
from math import ceil, log10

INP_PATH = 'test/07'
INP_PATH = 'input/07'

# read input as tuples of target variable and list of numbers
with open(INP_PATH) as file:
    inp = [(int(l.split(': ')[0]), list(map(int, l.split(': ')[1].split()))) for l in file.read().splitlines()]

# calculate the number of possible calibrations
def calibrations(target: int, lst: list, curr: int, part2: bool = False) -> int:
    if lst == [] or target < curr: # recursion stop + early break - curr is strictly increasing
        return target == curr
    # these two operators have to be done for both part 1 and part 2
    csum = calibrations(target, lst[1:], curr*lst[0], part2) + calibrations(target, lst[1:], curr+lst[0], part2)
    if part2:
        # for part 2, add the concatenation operator
        csum += calibrations(target, lst[1:], curr*10**ceil(log10(lst[0]+1))+lst[0], part2) 
    return csum

# part 1 answer: number of possible calibrations
pprint(sum(target for target, lst in inp if calibrations(target, lst[1:], lst[0])))

# part 2 answer: number of possible calibrations with concatenation also
pprint(sum(target for target, lst in inp if calibrations(target, lst[1:], lst[0], True)))