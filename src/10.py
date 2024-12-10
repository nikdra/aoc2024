from pprint import pprint
from collections import deque
from math import inf

INP_PATH = 'test/10'
INP_PATH = 'input/10'

 # read input as dict of points with height value
with open(INP_PATH) as file:
    inp = {(x,y): int(c) for y, line in enumerate(file.read().splitlines()) for x,c in enumerate(line)}

# only up, down, left, right
dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]

# find the score of a trail
# that is:
# - for part 1, the number of points that can be reached with height 9
# - for part 2, the number distinct ways we can reach a point with height 9
# for the correct result, we assume that the coordinate handed over to this function has height 0
def score(x: int, y: int, part2: bool = False):
    tails = set()  # distinct trail tails
    distinct = 0  # number of distinct paths
    q = deque()  # queue to hold our current path
    q.append((x,y))  
    while len(q) != 0:  # while we have paths to explore
        x, y = q.pop()  # take point
        if inp[(x,y)] == 9:
            # reached a trailhead, add to result(s)
            tails.add((x,y))
            distinct += 1
        neighbors = filter(lambda p: inp.get(p, inf) == inp[(x,y)] + 1, ((x+x1, y+y1) for (x1, y1) in dirs))  # reachable neighbors
        q.extend(neighbors)  # add to queue
    return len(tails) if not part2 else distinct  # depending on part 1 or part 2, return the result
        

# part 1 answer: number of distinct tails we can reach from each starting position
pprint(sum(score(*p) for p, v in inp.items() if v == 0))

# part 2 answer: number of distinct trails on the map
pprint(sum(score(*p, True) for p, v in inp.items() if v == 0))