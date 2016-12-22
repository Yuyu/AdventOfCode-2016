import numpy as np
import re
import sys
from itertools import permutations

with open("input.txt", "r") as fp:
    data = fp.read().strip().splitlines()[2:]

p1 = False
width, height = 37, 28

nodes = np.ndarray((width, height), dtype=tuple)
for line in data:
    args = line.split()
    total, used = map(lambda x: int(x[:-1]), args[1:3])
    x, y = map(int, re.sub("x|y", "", args[0]).split("-")[-2:])
    nodes[x, y] = (used, total)

if p1:
    pairs = set()
    for x1 in xrange(width):
        for y1 in xrange(height):
            if nodes[x1, y1][0] == 0:
                continue
            for x2 in xrange(width):
                for y2 in xrange(height):
                    if x1 == x2 and y1 == y2:
                        continue
                    if nodes[x2, y2][1] > nodes[x1, y1][0]:
                        pairs.add((x1, y1, x2, y2))

    print len(pairs)
else:
    # Part 2 I did by hand with this printed out
    # 14 + 25 + 28 + 5*36
    for y in xrange(height):
        for x in range(width):
            sys.stdout.write("{:3}/{:<3} ".format(*nodes[x, y]))
        print
