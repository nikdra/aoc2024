from pprint import pprint

INP_PATH = 'test/02'
INP_PATH = 'input/02'

# read input as list of lines (horizontally)
with open(INP_PATH) as file:
    inp = [list(map(int,l.split())) for l in file.readlines()]

# definition of safe:
# The levels are either all increasing or all decreasing
# Any two adjacent levels differ by at least one and at most three
def isSafe(report: list) -> bool:
    return all(r < s and 1 <= s-r <= 3 for (r,s) in zip(report[:-1], report[1:])) \
        or all(r < s and 1 <= s-r <= 3 for (s,r) in zip(report[:-1], report[1:]))

# print part 1 answer: the number of safe reports
pprint(sum(isSafe(r) for r in inp))

# definition of safety with problem dampener
# If removing a single level from an unsafe report would make it safe, the report instead counts as safe
def isSafeDampened(report:list) -> bool:
    # i _think_ this returns a value as soon as _one_ true value appears in the iterable
    return any(isSafe(report[0:i] + report[i+1:]) for i in range(len(report)))

# print part 2 answer: the number of safe reports after applying the problem dampener
pprint(sum(isSafeDampened(r) for r in inp))