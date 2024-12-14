f = open("input")
raw_data = f.read().split("\n")
f.close()

X = len(raw_data[0])
Y = len(raw_data)
FRAZE = "XMAS"
counter = 0 

#  -  horizontal
for s in raw_data:
    counter += s.count(FRAZE) + s.count(FRAZE[::-1])

#  |  vertical
for x in range(X):
    s = ""
    for y in range(Y):
        s += raw_data[y][x]
    counter += s.count(FRAZE) + s.count(FRAZE[::-1])

#  /  diagonals (1)
xs,ys = 0,0
while ys < Y:
    x,y,s = xs,ys,""
    while x >= 0 and y < Y:
        s += raw_data[y][x]
        x-=1
        y+=1
    if xs < X-1: xs+=1
    else: ys+=1
    counter += s.count(FRAZE) + s.count(FRAZE[::-1])

#  \  diagonals (-1)
xs,ys = 0,Y-1
while xs < X:
    x,y,s = xs,ys,""
    while x < X and y < Y:
        s += raw_data[y][x]
        x+=1
        y+=1
    if ys > 0 : ys -= 1
    else: xs += 1
    counter += s.count(FRAZE) + s.count(FRAZE[::-1])

print(counter)


# PART 2 

counter = 0
for y in range(0,Y-2):
    for x in range(0,X-2):
        d1 = "" + raw_data[y][x] + raw_data[y+1][x+1] + raw_data[y+2][x+2]
        d2 = "" + raw_data[y][x+2] + raw_data[y+1][x+1] + raw_data[y+2][x]
        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            counter += 1
print(counter)