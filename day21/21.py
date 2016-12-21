from itertools import permutations

with open("day21/input.txt", "r") as fp:
    instructions = fp.read().strip().splitlines()

def scramble(pw):
    pw = [x for x in pw]
    l = len(pw)

    for instruction in instructions:
        args = instruction.split()
        if args[0] == "move":
            x, y = map(int, [args[2], args[5]])
            c = pw[x]
            pw = pw[:x] + pw[x+1:]
            pw.insert(y, c)
        elif args[0] == "reverse":
            x, y = map(int, [args[2], args[4]])
            pw = pw[:x] + pw[x:y+1][::-1] + pw[y+1:]
        elif args[0] == "swap":
            if args[1] == "position":
                x, y = map(int, [args[2], args[5]])
                c = pw[x]
                pw[x] = pw[y]
                pw[y] = c
            else:
                x, y = args[2], args[5]
                for i in range(l):
                    if pw[i] == x:
                        pw[i] = y
                    elif pw[i] == y:
                        pw[i] = x
        elif args[0] == "rotate":
            if args[1] == "based":
                x = args[6]
                y = pw.index(x)
                y = (y + (2 if y >= 4 else 1)) % l
                pw = pw[-y:] + pw[:-y]
            else:
                x = int(args[2]) % l
                if args[1] == "left":
                    pw = pw[x:] + pw[:x]
                else:
                    pw = pw[-x:] + pw[:-x]

    return "".join(pw)

p1 = False
if p1:
    print scramble("abcdefgh")
else:
    search = "fbgdceah"
    for pw in permutations("abcdefgh"):
        if scramble(pw) == search:
            print "".join(pw)
            break
