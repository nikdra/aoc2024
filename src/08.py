from pprint import pprint
from itertools import combinations

INP_PATH = 'test/08'
INP_PATH = 'input/08'

with open(INP_PATH) as file:
    inp = {(x,y): v for y, line in enumerate(file.read().splitlines()) for x, v in enumerate(line)}

# given a frequency, return the set of antinodes on the map
def antinodes(frequency: str) -> set:
    nodes = set(p for p, v in inp.items() if v == frequency)  # find the antennas/nodes of this frequency
    anti = set()  # set of antinodes for this set of antennas
    pairs = combinations(nodes, 2)  # get all pairs of antennas
    for (a,b) in pairs:
        vec = a[0] - b[0], a[1] - b[1]  # calculate vector between antennas
        anti.add((a[0]+ vec[0], a[1] + vec[1]))  # add to first antenna
        anti.add((b[0]- vec[0], b[1] - vec[1]))  # add to second antenna (reversed)
    return set(filter(lambda p: p in inp.keys(), anti))  # only consider antinodes on the map

# calculate part 1 answer: all distinct antinode points for all frequencies
part1 = set()
for antis in (antinodes(f) for f in set(v for v in inp.values() if v != '.')):
    part1.update(antis)

# print part 1 answer
pprint(len(part1))

# given a frequency, return the set of antinodes on the map - with harmonies
def antinodesHarmonized(frequency: str) -> set:
    nodes = set(p for p, v in inp.items() if v == frequency)  # find the antennas/nodes of this frequency
    anti = set()  # set of antinodes for this set of antennas
    pairs = combinations(nodes, 2)  # get all pairs of antennas
    for (a,b) in pairs:
        vec = a[0] - b[0], a[1] - b[1]  # calculate vector between antennas
        # add vector to first antenna until we go off the map
        curr = a
        while curr in inp.keys():
            anti.add(curr)
            curr = (curr[0]+ vec[0], curr[1] + vec[1])
        # add reversed vector to second antenna until we go off the map
        curr = b
        while curr in inp.keys():
            anti.add(curr)
            curr = (curr[0]- vec[0], curr[1] - vec[1])
    # these points are all on the map
    return anti

# calculate part 1 answer: all distinct antinode points for all frequencies
part2 = set()
for antis in (antinodesHarmonized(f) for f in set(v for v in inp.values() if v != '.')):
    part2.update(antis)

# print part 1 answer
pprint(len(part2))