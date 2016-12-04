import string
import collections

with open("input.txt", "r") as fp:
    data = fp.read().strip()
    lines = data.split("\n")

def shift(room, sector):
    shift = sector % 26
    table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    return room.translate(table)

sector_sum = 0
for line in lines:
    vals = line.split("-")
    room = "".join(vals[:-1])
    room_with_dashes = "-".join(vals[:-1])
    sector = int(vals[-1].split("[")[0])
    checksum = vals[-1].split("[")[1][:-1]

    occurences = sorted((-v,k) for k,v in collections.Counter(room).most_common())
    calculated_checksum = "".join(v for k,v in occurences[:5])

    if calculated_checksum == checksum:
        sector_sum += sector

        decrypted_room = shift(room_with_dashes, sector)
        if "north" in decrypted_room and "pole" in decrypted_room:
            print decrypted_room, sector

print sector_sum
