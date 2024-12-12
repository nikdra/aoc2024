from pprint import pprint
from collections import Counter

INP_PATH = 'test/11'
INP_PATH = 'input/11'

# read input as dict of stones: number of stones
with open(INP_PATH) as file:
    inp = Counter(map(int, file.readline().strip().split(' ')))


# blink ones with the given stones
def blink(stones: dict) -> dict:
    next = {}  # dict of the stones after blinking
    # important note: all updates happen simultaneously and independently
    # we do the updates for all stones with the same engraving and add the result to the return variable
    for stone, num in stones.items():
        stringStone = str(stone)
        if stone == 0:
            next[1] = next.get(1, 0) + num  # all stones with number 0 become stones with number 1
        elif len(stringStone) % 2 == 0:
            # stones with a number that has even length are split into even parts
            next[int(stringStone[:len(stringStone) // 2])] = next.get(int(stringStone[:len(stringStone) // 2]), 0) + num
            next[int(stringStone[len(stringStone) // 2:])] = next.get(int(stringStone[len(stringStone) // 2:]), 0) + num
        else:
            # none of the rules apply: stones are multiplied with 2024
            next[stone * 2024] = next.get(stone * 2024, 0) + num
    return next


# recursive function to blink num times
def blinks(stones: dict, num: int) -> dict:
    if num == 0:
        return stones
    return blinks(blink(stones), num-1)

# return part 1 answer: number of stones after 25 blinks
pprint(sum(v for v in blinks(inp, 25).values()))

# return part 2 answer: number of stones after 75 blinks
# it's a pretty big number, which is why we used a dict to do all the updates simultaneously
pprint(sum(v for v in blinks(inp, 75).values()))

# just a check how many distinct engravings there are because i'm curious
pprint(len(blinks(inp, 75).keys()))