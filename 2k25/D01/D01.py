f = open("input.txt","r")
rotations = f.read().split()
f.close()

pos = 50
exact_zeros = 0
clicked_zeros = 0

for rot in rotations:
    start_pos = pos
    direction = rot[0]
    value = int(rot[1:])
    full_rotations = value//100
    clicked_zeros += full_rotations
    value %= 100

    if direction == "R": pos += value
    if direction == "L": pos -= value

    if pos < 0 or pos > 99:
        if start_pos!=0 and pos%100!=0:
            clicked_zeros += 1
        pos %= 100

    if pos == 0: exact_zeros += 1

print(exact_zeros)
print(exact_zeros + clicked_zeros)