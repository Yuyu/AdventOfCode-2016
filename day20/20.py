p1 = False

with open("input.txt", "r") as fp:
    data = fp.read().strip().split("\n")

ranges = [(map(int, r.split("-"))) for r in data]
ranges.sort()

allowed, i, r = 0, 0, 0
while i < 2**32:
    l, h = ranges[r]
    if i >= l:
        if i <= h:
            i = h + 1
            continue
        r += 1
    else:
        if p1:
            print i
            exit()
        allowed += 1
        i += 1

print allowed
