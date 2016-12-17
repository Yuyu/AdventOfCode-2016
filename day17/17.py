from hashlib import md5

inp = "gdjjyniy"

directions = {"U": 0, "D": 1, "L": 2, "R": 3}
vectors = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}
valid = ["b", "c", "d", "e", "f"]

ways = []
end = (3, 3)

h = md5(inp).hexdigest()[:4]
ways.extend((0, 0, d) for (d, i) in filter(lambda (k, v): h[v] in valid, directions.iteritems()))

while len(ways) != 0:
    new = []
    for (x, y, d) in ways:
        x += vectors[d[-1]][0]
        y += vectors[d[-1]][1]
        if x < 0 or y < 0 or x > 3 or y > 3:
            continue
        if (x, y) == end:
            # Part 1
            # print d
            # exit()
            continue

        h = md5(inp+d).hexdigest()[:4]

        new.extend((x, y, d+n_d) for (n_d, i) in filter(lambda (k, v): h[v] in valid, directions.iteritems()))

    ways = new

print d
