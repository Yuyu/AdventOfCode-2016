floors_p1 = [8, 2, 0, 0]
floors_p2 = [12, 2, 0, 0]

print "Part #1:", sum(2 * sum(floors_p1[:x]) - 3 for x in range(1, 4))
print "Part #2:", sum(2 * sum(floors_p2[:x]) - 3 for x in range(1, 4))
