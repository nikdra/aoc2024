from pprint import pprint

INP_PATH = 'test/06'
INP_PATH = 'input/06'

# read the map as a map
with open(INP_PATH) as file:
    inp = {(x,y): c for y,l in enumerate(file.read().splitlines()) for x,c in enumerate(l)} 

# directions 
dirs = {
    'u': (0, -1),
    'r': (1, 0),
    'd': (0, 1),
    'l': (-1, 0)
}

# changes in directions - from up go right, from right go down etc
dir_changes = {
    'u': 'r',
    'r': 'd',
    'd': 'l',
    'l': 'u'
}

# number of distinct postions until the guard goes out of bounds
def distinctPositions() -> int:
    positions = set()  # positions we've visited
    pos = next(k for k,v in inp.items() if v == '^')  # starting position of the guard/current position
    inpMap = {k:v if v != '^' else '.' for k,v in inp.items()}  # remove starting position with '.'
    dir = 'u'  # current direction
    while pos in inpMap.keys():  # while in bounds 
        positions.add(pos)  # add position
        x, y = pos 
        pos = x + dirs[dir][0], y + dirs[dir][1]  # move
        if inpMap.get(pos, 'X') == 'X':  # out of bounds - exit loop
            return len(positions)
        if inpMap[pos] == '#':  # obstruction - change direction and move back to previous position
            dir = dir_changes[dir]
            pos = x, y
            continue
        
# part 1 answer: print the number of distinct positions the guard visits before leaving
pprint(distinctPositions())

# part 2: brute force i guess
        
# basically the same function as above, but we store the position as well
# the only parameter is the obstruction we add to the map
def createsLoop(objectPos: tuple) -> bool:
    positions = set()  # positions we've visited
    pos = next(k for k,v in inp.items() if v == '^')  # starting position of the guard/current position
    inpMap = {k:v if v != '^' else '.' for k,v in inp.items()}  # remove starting position with '.'
    inpMap[objectPos] = '#' # add obstruction
    dir = 'u'  # current direction
    while pos in inpMap.keys():  # while in bounds 
        if (pos, dir) in positions:  # if we've been here before with this direction, it's a loop
            return True
        positions.add((pos, dir))  # add position and direction
        x, y = pos 
        pos = x + dirs[dir][0], y + dirs[dir][1]  # move
        if inpMap.get(pos, 'X') == 'X':  # out of bounds - exit loop
            return False
        if inpMap[pos] == '#':  # obstruction - change direction and move back to previous position
            dir = dir_changes[dir]
            pos = x, y
            continue

# print part 2 answer (takes a bit): number of loops we can create by adding one obstruction
pprint(sum(createsLoop(pos) for pos in inp.keys() if inp[pos] == '.'))