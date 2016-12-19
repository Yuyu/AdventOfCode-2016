# Implementation using a circular linked list
# Runs 10 times as fast with pypy (7,84s, 0,78s),
# so it's actually faster than the other solution (4,48s, 0,98s)

from time import time

inp = 3014603

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

l = map(Node, xrange(1, inp + 1))
for i in xrange(0, inp):
    l[i].next = l[(i + 1) % inp]
    l[i].prev = l[(i - 1) % inp]

n = l[0]
while n.next != n:
    n.next = n.next.next
    n.next.next.prev = n
    n = n.next

print n.data
