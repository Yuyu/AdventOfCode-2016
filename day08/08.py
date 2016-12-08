import re
import time
import sys

with open("input.txt", "r") as fp:
    data = fp.read().strip()

screen_width = 50
screen_height = 6
screen = [[" " for _ in range(screen_width)] for _ in range(screen_height)]

for instruction in data.split("\n"):
    if instruction.startswith("rect"):
        width, height = map(int, re.findall(r"(\d+)x(\d+)", instruction)[0])
        for y in range(height):
            for x in range(width):
                screen[y][x] = "x"
    elif instruction.startswith("rotate row"):
        y, num = map(int, re.findall(r"(\d+) by (\d+)", instruction)[0])
        screen[y] = screen[y][-num:] + screen[y][:-num]
    elif instruction.startswith("rotate column"):
        x, num = map(int, re.findall(r"(\d+) by (\d+)", instruction)[0])
        screen = map(list, zip(*screen)) # transpose the screen
        screen[x] = screen[x][-num:] + screen[x][:-num]
        screen = map(list, zip(*screen)) # and turn it back

    sys.stdout.write("\033c")
    print "\n".join("".join(x for x in row) for row in screen)
    time.sleep(.05)

print "Pixels on fire:", sum(1 if x == "x" else 0 for row in screen for x in row)
