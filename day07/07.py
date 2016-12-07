import re

def abba(x):
    return x == x[::-1] and x[0] != x[1]

with open("input.txt", "r") as fp:
    data = fp.read().strip()

results_p1 = 0
results_p2 = 0
for line in data.split("\n"):
    parts = re.split(r"\[|\]", line.strip())

    # Part 1
    results = [[], []]

    for part in parts[::2]:
        for i in xrange(0, len(part)-3):
            results[0].append(abba(part[i:i+4]))

    for part in parts[1::2]:
        for i in xrange(0, len(part)-3):
            results[1].append(abba(part[i:i+4]))

    if any(results[0]) and not any(results[1]):
        results_p1 += 1

    # Part 2
    reqs = []
    results = []

    for part in parts[::2]:
        for i in xrange(0, len(part)-2):
            if abba(part[i:i+3]):
                reqs.append(part[i+1]+part[i]+part[i+1])

    for part in parts[1::2]:
        for i in xrange(0, len(part)-2):
            results.append(part[i:i+3] in reqs)

    if any(results):
        results_p2 += 1

print "Part 1:", results_p1
print "Part 2:", results_p2
