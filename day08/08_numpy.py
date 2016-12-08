import numpy as np

with open("input.txt", "r") as fp:
    data = fp.read().strip()

screen = np.zeros([6, 50], dtype=bool)

for line in data.split("\n"):
    params = line.split()
    if params[0] == "rect":
        width, height = map(int, params[1].split("x"))
        screen[:height, :width] = True
    else:
        xy, n = map(int, line.split("=")[1].split(" by "))
        if params[1] == "row":
            screen[xy] = np.roll(screen[xy], n)
        else:
            screen.T[xy] = np.roll(screen.T[xy], n)

print "\n".join("".join("X" if x else "." for x in row) for row in screen)
print np.sum(screen)
