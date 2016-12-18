import numpy as np

inp = ".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."
rows = 40 # 40 for Part 1, 400000 for Part 2

tiles = np.ndarray((102, rows), dtype=bool)
# I've added one extra add both sides to include the "imaginary safe tiles"
tiles[:, 0] = [True] + map(lambda x: x == ".", list(inp)) + [True]

for y in xrange(1, rows):
    tiles[:, y] = [True] + map(lambda x: tiles[x-1, y-1] == tiles[x+1, y-1], xrange(1, 101)) + [True]

# Subtract the imaginary safe tiles from the total sum of safe places
print np.sum(tiles)-rows*2
