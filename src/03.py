from pprint import pprint
import re

INP_PATH = 'test/03'
INP_PATH = 'input/03'

# read input as one thing
with open(INP_PATH) as file:
    inp = file.read()

# regex stuff: find all mul(number, number pairs)
mats = re.findall(r"mul\(\d+,\d+\)", inp)
# part 1 answer: print the sum of the product of pairs
pprint(sum(x * y for x,y in (map(int, m[4:-1].split(',')) for m in mats)))

# regex stuff: find find all mul(number, number pairs) and the do/don't instructions
mats = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", inp)

# iterate through the matches and sum up all the "enabled" instructions
ok = True # at the beginning of the program, instructions are enabled
res = 0 # result running variable
for m in mats:
    if m == 'do()':
        ok = True # enable instructions
    elif m == 'don\'t()':
        ok = False # disable instructions
    else:
        if ok: # if enabled
            x,y =  map(int, m[4:-1].split(',')) # get the pair
            res += x * y # add the product to the result running variable

# part 2 answer
pprint(res)