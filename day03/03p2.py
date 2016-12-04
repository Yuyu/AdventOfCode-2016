with open("input.txt", "r") as fp:
    data = fp.read().strip()
    lines = data.split("\n")

correct = 0
i = 0
while i < len(lines):
    values = []
    for j in range(i, i + 3):
        values.append(sorted([int(x) for x in lines[j].split()]))
    for j in range(0, 3):
        correct = correct + (1 if values[0][j] + values[1][j] > values[2][j] else 0)
    i += 3

print correct
