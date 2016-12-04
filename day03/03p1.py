with open("input.txt", "r") as fp:
    data = fp.read().strip()
    lines = data.split("\n")

correct = 0
for line in lines:
    values = sorted([int(x) for x in line.split()])
    correct = correct + (1 if values[0] + values[1] > values[2] else 0)

print correct
