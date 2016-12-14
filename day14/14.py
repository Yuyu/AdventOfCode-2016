import hashlib
import re
import sys

salt = "jlmsuwbz"
part = 2

hashes = []
keys = []
idx = 0
r = re.compile(r"(\w)\1\1")

def gen(i):
    try:
        return hashes[i]
    except:
        h = hashlib.md5(salt + str(i)).hexdigest()
        if part == 2:
            for _ in xrange(2016):
                h = hashlib.md5(h).hexdigest()
        hashes.append(h)
        return h

while len(keys) < 64:
    h = gen(idx)
    c = r.findall(h)
    if len(c) > 0:
        c = c[0]*5 # only consider the first match
        for j in xrange(idx+1, idx+1001):
            hc = gen(j)
            if c in hc:
                keys.append(h)
                break

    sys.stdout.write(hashes[idx] + ", idx " + str(idx) + ", found " + str(len(keys)) + "\r")

    idx += 1

print
