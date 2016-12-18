import numpy as np

# I've added one extra add both sides to include the "imaginary safe tiles"
inp = ".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."
rows = 40 # 40 for Part 1, 400000 for Part 2

tiles = np.ndarray((102, rows), dtype=bool)
tiles[:, 0] = [True] + map(lambda x: x == ".", list(inp)) + [True]

for y in xrange(1, rows):
    tiles[:, y] = [True] + map(lambda x: not ((not tiles[x-1, y-1] and tiles[x+1, y-1]) \
        or (tiles[x-1, y-1] and not tiles[x+1, y-1])), xrange(1, 101)) + [True]

# Subtract the imaginary safe tiles from the total sum of safe places
print np.sum(tiles)-rows*2
