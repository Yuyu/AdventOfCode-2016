import hashlib

inp = "cxdnnyjw"

print "".join(x[5] for x in filter(lambda x: x.startswith("00000"), [hashlib.md5(inp + str(i)).hexdigest() for i in xrange(10000000)])[:8])

#pw = ""
#for i in xrange(100000000):
#    x = inp + str(i)
#    h = hashlib.md5(x).hexdigest()
#    if h.startswith("00000"):
#        pw += h[5]
#        if len(pw) == 8:
#            break

#print pw
