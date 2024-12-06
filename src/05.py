from pprint import pprint
from functools import cmp_to_key

INP_PATH = 'test/05'
INP_PATH = 'input/05'

# read input as map of rules and lists of updates
with open(INP_PATH) as file:
    rs, updates = file.read().split('\n\n')
    # careful: a number can be ordered before multiple numbers
    # e.g. 99: [1,2,3,4] => 99 has to go before 1,2,3 or 4
    rules = {i: [] for i in range(100)} # assumption max 100
    for l in rs.split('\n'):
        for k,v in [l.split('|')]:
            rules[int(k)] += [int(v)]
    # read updates as a list each
    updates = [list(map(int,l.split(','))) for l in updates.split()]

def customSorted(update:list) -> list:
    # custom sort defined by the rules - cmp_to_key translates our rules to a key for comparison
    # sorted is a stable function! (and therefore fit for use here)
    return sorted(update, key=cmp_to_key(lambda a,b: -1 if b in rules.get(a) else 0))

def orderedUpdate(update: list) -> bool:
    # an update is sorted if the list is the same as its sorted version
    return update == customSorted(update)

# part 1 answer: sum of middle elements of already correctly sorted lists
pprint(sum(u[int(len(u)/2)] for u in updates if orderedUpdate(u)))

# part 2 answer: sum of middle elements of incorrectly sorted lists, sorted to our rules
pprint(sum(customSorted(u)[int(len(u)/2)] for u in updates if not orderedUpdate(u)))