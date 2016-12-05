import hashlib

inp = "cxdnnyjw"

pw = [""]*8
i = 0
while True:
    x = inp + str(i)
    h = hashlib.md5(x).hexdigest()
    if h.startswith("00000"):
        pos = int(h[5], 16)
        if pos < 8 and pw[pos] == "":
            pw[pos] = h[6]
            if "" not in pw:
                break

    i += 1

print "".join(pw)
