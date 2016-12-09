with open("input.txt", "r") as fp:
    data = fp.read().strip()

i = 0
l = 0
while i < len(data):
    np = data.find("(", i)
    ncp = data.find(")", np)
    if np < 0 or ncp < 0:
        l += len(data) - i
        break
    ml, mc = map(int, data[np+1:ncp].split("x"))
    l += np - i
    l += ml * mc
    i = ncp + 1 + ml

print l
