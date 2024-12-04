from pprint import pprint

INP_PATH = 'test/04'
INP_PATH = 'input/04'

# read input as map of points with character value (makes search easier imo)
# x is the horizontal coordinate, y the vertical coordinate
with open(INP_PATH) as file:
    inp = {(x,y): v for y,l in enumerate(file.read().splitlines()) for x,v in enumerate(l)}

# search for the word 'XMAS' in every possible direction 
def search(x: int, y: int) -> int:
    # find all possible candidate coordinates (this can probably be made easier)
    hor = [[(x,y1) for y1 in range(y,y+4)]] + [list(reversed([(x,y1) for y1 in range(y-3,y+1)]))]
    vert = [[(x1,y) for x1 in range(x,x+4)]] + [list(reversed([(x1,y) for x1 in range(x-3,x+1)]))]
    m1 = [[(x+i, y+i) for i in range(4)]] + [[(x-i,y-i) for i in range(4)]]
    m2 = [[(x-i, y+i) for i in range(4)]] + [[(x+i,y-i) for i in range(4)]]
    # return the number of times we found the word XMAS originating from this position
    return sum(w == 'XMAS' for w in (''.join(inp.get(p, '.') for p in c) for c in hor + vert + m1 + m2))

# part 1 answer
# it only makes sense to search if the coordinate has the letter 'X'
pprint(sum(search(*k) for k,v in inp.items() if v == 'X'))

# find the word 'MAS' in a cross like
# M.S
# .A.
# M.S
def xmasSearch(x: int, y:int) -> bool:
    # we look at the four three-letter words that cross this coordinate
    m1 = [[(x+i, y+i) for i in range(-1,2,1)]] + [[(x-i,y-i) for i in range(-1,2,1)]]
    m2 = [[(x-i, y+i) for i in range(-1,2,1)]] + [[(x+i,y-i) for i in range(-1,2,1)]]
    # see if any of the crosses match 'MAS'
    cross1 = any(w == 'MAS' for w in (''.join(inp.get(p, '.') for p in c) for c in m1))
    cross2 = any(w == 'MAS' for w in (''.join(inp.get(p, '.') for p in c) for c in m2))
    # if they both match 'MAS', we have X-MAS!
    return cross1 and cross2

# part 2 answer
# it only makes sense to search if the coordinate has the letter 'A'
pprint(sum(xmasSearch(*k) for k,v in inp.items() if v == 'A'))