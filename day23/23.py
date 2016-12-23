import sys
from copy import copy

p1 = False

with open("input.txt", "r") as fp:
    data = fp.read().strip()

code = [x.split() for x in data.split("\n")]
toggled = [False for x in code]

registers = {
    "a": 12, "b": 0, "c": 0, "d": 0 # a = 7 for Part 1, 12 for Part 2
}

def value_or_register(x):
    if x in registers.keys():
        return registers[x]
    else:
        return int(x)

def is_register(x):
    return x in registers.keys()

cp = 0
l = len(code)
while cp < l:
    args = copy(code[cp])

    # "Optimization" for Part 2
    if not p1 and cp == 4:
        registers["a"] = registers["b"] * registers["d"]
        registers["c"] = 0
        registers["d"] = 0
        cp = 10
        continue

    is_toggled = toggled[cp]
    if is_toggled:
        if args[0] == "inc":
            args[0] = "dec"
        elif args[0] == "dec" or args[0] == "tgl":
            args[0] = "inc"
        elif args[0] == "cpy":
            args[0] = "jnz"
        elif args[0] == "jnz":
            args[0] = "cpy"

        if (args[0] == "cpy" and not is_register(args[2])) \
            or ((args[0] == "inc" or args[0] == "dec") and not is_register(args[1])):
            cp += 1
            continue

    if args[0] == "cpy":
        registers[args[2]] = value_or_register(args[1])
    elif args[0] == "inc":
        registers[args[1]] += 1
    elif args[0] == "dec":
        registers[args[1]] -= 1
    elif args[0] == "jnz":
        if value_or_register(args[1]) != 0:
            cp += value_or_register(args[2])
            continue
    elif args[0] == "tgl":
        x = value_or_register(args[1])
        y = cp + x
        if y >= l:
            cp += 1
            continue
        toggled[y] = not toggled[y]

    cp += 1

print registers
