fp = open("input.txt", "r")
data = fp.read().strip()
fp.close()

data = data.split(", ")

movement = ((0, -1), (1, 0), (0, 1), (-1, 0))
facing = 0

visited = []
pos = (0,0)
visited.append(pos)

for m in data:
    turn = m[0]
    blocks = int(m[1:])

    facing = (facing + 1) % 4 if turn == "R" else (facing - 1) % 4

    for _ in xrange(0, blocks):
        pos = (pos[0] + movement[facing][0], pos[1] + movement[facing][1])
        if pos in visited:
            print abs(pos[0]) + abs(pos[1])
            exit()
        else:
            visited.append(pos)
