with open("input.txt", "r") as fp:
    data = fp.read().strip()

def decompress(d):
    l = 0
    i = 0
    while i < len(d):
        if d[i] == "(":
            j = d.find(")", i)
            ml, mc = map(int, d[i+1:j].split("x"))
            l += decompress(d[j+1:j+1+ml]) * mc
            i = j + 1 + ml
        else:
            l += 1
            i += 1
    return l

print decompress(data)
