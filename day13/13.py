num = 1362
end = (31, 39)
visited = set()
path = [(1, 1)]
steps = 0

def is_wall(x, y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + num).count("1") % 2 == 1

while end not in path:
    new = []
    for (x, y) in path:
        visited.add((x, y))
        if x != 0 and (x-1, y) not in visited and not is_wall(x-1, y):
            new.append((x-1, y))
        if (x+1, y) not in visited and not is_wall(x+1, y):
            new.append((x+1, y))
        if y != 0 and (x, y-1) not in visited and not is_wall(x, y-1):
            new.append((x, y-1))
        if (x, y+1) not in visited and not is_wall(x, y+1):
            new.append((x, y+1))
    path = new
    steps += 1
    if steps == 51: # 51 because I append them to the visited list after the next iteration
        print "Part #2:", len(visited)

print "Part #1:", steps
