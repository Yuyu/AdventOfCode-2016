disks = []
for line in open("input.txt", "r").read().strip().split("\n"):
    args = line.split()
    disks.append((int(args[3]), int(args[-1][:-1])))

# Part 2
disks.append((11, 0))

time = 0
while sum((y + time + t) % x for t, (x, y) in enumerate(disks, 1)) != 0:
    time += 1

print time
