fp = open("input.txt", "r")
data = fp.read().strip()
fp.close()

data = data.split(", ")

facing = 0
directions_walked = [0, 0, 0, 0]

for m in data:
    turn = m[0]
    blocks = int(m[1:])
    facing = (facing + 1) % 4 if turn == "R" else (facing - 1) % 4
    directions_walked[facing] += blocks

print abs(directions_walked[2] - directions_walked[0]) + abs(directions_walked[1] - directions_walked[3])
