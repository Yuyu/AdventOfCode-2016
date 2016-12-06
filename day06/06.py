import collections

with open("input.txt", "r") as fp:
    data = fp.read().strip().split("\n")

# Part 1
print "".join(collections.Counter(x).most_common()[0][0] for x in zip(*data))

# Part 2
print "".join(collections.Counter(x).most_common()[-1][0] for x in zip(*data))
