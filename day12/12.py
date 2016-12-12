with open("input.txt", "r") as fp:
    data = fp.read().strip()

code = [x.split() for x in data.split("\n")]
registers = {
    "a": 0, "b": 0, "c": 1, "d": 0 # c = 0 for Part 1, c = 1 for Part 2
}

def value_or_register(x):
    if x in registers.keys():
        return registers[x]
    else:
        return int(x)

cp = 0
while cp < len(code):
    args = code[cp]
    if args[0] == "cpy":
        registers[args[2]] = value_or_register(args[1])
    elif args[0] == "inc":
        registers[args[1]] += 1
    elif args[0] == "dec":
        registers[args[1]] -= 1
    elif args[0] == "jnz":
        if value_or_register(args[1]) != 0:
            cp += int(args[2])
            continue

    cp += 1

print registers
