f = open("input")
raw_data = f.read().split("\n")
f.close()

FRAZE = "XMAS"
counter = 0 
# left right & right left
for row in raw_data:
    matches = row.count(FRAZE) + row.count(FRAZE[::-1])
    counter += matches

# up down & down up
for x in range(len(raw_data[0])):
    string = ""
    for y in range(len(raw_data)):
        string += raw_data[y][x]
    matches = string.count(FRAZE) + string.count(FRAZE[::-1])
    counter += matches

N = len(raw_data)

for b in range(0,2*N - 1):
    string = ""
    for x in range(0,N):
        for y in range(0,N):
            if y == -1 * x + b:
                # print(f"{y}{x} ",end="")
                string += raw_data[y][x]
    # print()
    # print(string)
    matches = string.count(FRAZE) + string.count(FRAZE[::-1])
    counter += matches


for b in range(0-(N-1),N):
    string = ""
    for x in range(0,N):
        for y in range(0,N):
            if y == 1 * x + b:
                # print(f"{y}{x} ",end="")
                string += raw_data[y][x]
    # print()
    # print(string)
    matches = string.count(FRAZE) + string.count(FRAZE[::-1])
    counter += matches

print(counter)
