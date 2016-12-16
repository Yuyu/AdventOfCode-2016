from copy import copy

inp = "01111001100111011"
length = 35651584

while len(inp) < length:
    a = inp
    b = copy(a)
    b = "".join(map(lambda x: "1" if x is "0" else "0", b[::-1]))
    inp = a + "0" + b

inp = inp[:length]
while len(inp) % 2 == 0:
    checksum = ""
    for i in xrange(0, len(inp), 2):
        checksum += "1" if inp[i] == inp[i+1] else "0"
    inp = checksum

print inp
