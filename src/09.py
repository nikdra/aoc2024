# i don't want to talk about this.
# this is probably one of the worst ones out there.
from pprint import pprint
from itertools import starmap

INP_PATH = 'test/09'
INP_PATH = 'input/09'

# read input as the "extended" disk like in the input
# 2333133121414131402 becomes 00...111...2...333.44.5555.6666.777.888899 (where dots are None)
with open(INP_PATH) as file:
    line = file.read().strip()
    inp = [i//2 if i%2 == 0 else None for i, c in starmap(lambda a,b: (a, int(b)), enumerate(line)) for _ in range(c)]

# i guess this is "optimal" because we only need two pointers
def organize():
    disk = [c for c in inp]  # create a copy
    # i and j are pointers from each end, left/right respectively
    i = 0
    for j in range(len(disk)-1,-1,-1):
        if disk[j] is None:  # empty space, move left
            continue
        while disk[i] is not None:  # nonempty space, move right
            i += 1
            if i == len(disk):  # exceeded memory
                break
        if i >= j:  # nothing to move any more
            break
        # move fragment from right to left
        disk[i] = disk[j]
        disk[j] = None
    return disk

# print part 1 answer - checksum is sum of block id * position
pprint(sum(i*b for i,b in enumerate(organize()) if b is not None))

# oh no.
# jesus christ.
# i debugged this for longer than i want to admit until i figured out files have to move to the _left_
# try finding the place where the bug was hidden!
# if it wasn't clear, this takes a while
def organizeDefragmented():
    disk = [c for c in inp]  # create a copy
    blocks = {id: [] for id in set(c for c in inp if c is not None)}
    spaces = set()  # set of empty spaces - could probably be a heap or heaps
    space = None
    # find the indexes of spaces and files
    # technically optimal O(n)
    for i in range(len(disk)):
        if disk[i] is None and space is None:
            space = i
        elif disk[i] is not None and space is not None:
            # store the length, start and end of each space
            spaces.add((i-space, (space, i-1)))
            space = None
        if disk[i] is not None:
            blocks[disk[i]] += [i]
    # store the start and end of each block
    blocks = {id: (v[0], v[-1]) for id, v in blocks.items()}
    # move em
    for id in sorted(blocks, reverse=True):
        start, end = blocks[id]
        step = end-start+1
        # find the space to move to - it has to be to the left of the current block!
        # this is where a heap would be good
        moves = sorted(list(filter(lambda x: x[0] >= step and x[1][1] < start, spaces)), key=lambda x: x[1][0])
        moveTo = None if len(moves) == 0 else moves[0]
        # if we have a place to move, move
        if moveTo is not None:
            moveToStart, moveToEnd = moveTo[1]
            spaces.remove(moveTo)  # remove space from our set of free spaces
            disk[moveToStart:moveToStart+step] = disk[start:end+1]
            disk[start:end+1] = [None for _ in range(step)]
            # if we did not take the full free space, return the rest to our free space
            if moveTo[0] > step:
                spaces.add((moveTo[0]-step, (moveToStart+step, moveToEnd)))
    return disk 

# print part 2 answer - checksum is sum of block id * position
pprint(sum(i*b for i,b in enumerate(organizeDefragmented()) if b is not None))