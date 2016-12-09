with open("input.txt", "r") as fp:
    data = fp.read().strip()

p1 = False

def decompress(d):
    i = 0
    l = 0
    while i < len(d):
        np = d.find("(", i)
        ncp = d.find(")", np)

        if np < 0 or ncp < 0:
            l += len(d) - i
            break

        ml, mc = map(int, d[np+1:ncp].split("x"))
        l += np - i
        l += (ml if p1 else decompress(d[ncp+1:ncp+1+ml])) * mc
        i = ncp + 1 + ml

    return l

print decompress(data)
