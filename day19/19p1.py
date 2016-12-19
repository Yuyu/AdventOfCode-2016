inp = 3014603

elves = [True]*inp

def next_index(i):
    while not elves[i]:
        i = (i + 1) % inp
    return i

i = 0
n = inp
while n != 1:
    j = next_index((i + 1) % inp)
    elves[j] = False
    i = next_index(j)
    n -= 1

print i+1
