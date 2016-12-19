from collections import deque

inp = 3014603

# l is a stack, r is a queue
l, r = (deque(), deque())

for i in xrange(1, inp/2+2):
    l.append(i)

for i in xrange(inp/2+2, inp+1):
    r.appendleft(i)

while l and r:
    if len(l) > len(r): l.pop()
    else: r.pop()

    # rotate/fix positions
    r.appendleft(l.popleft())
    l.append(r.pop())

print l[0] or r[0]
