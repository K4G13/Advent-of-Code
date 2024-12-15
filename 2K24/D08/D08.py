file = open("input")
raw_data = file.read().split("\n")
file.close()

antenas = [list(row) for row in raw_data]
antinodes = [["." for el in row] for row in raw_data]
X,Y = len(raw_data[0]),len(raw_data)

frequencies = {}
for y in range(len(antenas)):
    for x in range(len(antenas[0])):

        freq = antenas[y][x]
        if freq == ".": continue

        if freq not in frequencies: frequencies[freq] = []
        frequencies[freq].append((x,y))

for freq,points in frequencies.items():
    # print(freq)
    for pointA in points:
        for pointB in points:
            if pointA == pointB: continue
            # print(pointA,pointB,end=" ")
            vecAB = [pointB[0] - pointA[0],pointB[1] - pointA[1]]
            vecBA = [pointA[0] - pointB[0],pointA[1] - pointB[1]]
            # print(vecAB,vecBA,end=" ")

            pointC = (pointB[0] + vecAB[0], pointB[1] + vecAB[1])
            pointD = (pointA[0] + vecBA[0], pointA[1] + vecBA[1])           
            # print(pointC,pointD) 

            if  pointC[0] >= 0 and pointC[0] < X and\
                pointC[1] >= 0 and pointC[1] < Y:
                antinodes[pointC[1]][pointC[0]] = "#"

            if  pointD[0] >= 0 and pointD[0] < X and\
                pointD[1] >= 0 and pointD[1] < Y:
                antinodes[pointD[1]][pointD[0]] = "#"

count = 0
for y in range(Y):
    for x in range(X):
        print(antinodes[y][x],end="")
        if antinodes[y][x] == "#": count += 1
    print()

print(count)

# PART 2

antinodes = [["." for el in row] for row in raw_data]

for freq,points in frequencies.items():
    # print(freq)
    for pointA in points:
        for pointB in points:
            if pointA == pointB: continue
            # print(pointA,pointB,end=" ")
            vecAB = [pointB[0] - pointA[0],pointB[1] - pointA[1]]
            vecBA = [pointA[0] - pointB[0],pointA[1] - pointB[1]]
            # print(vecAB,vecBA,end=" ")
            
            i = 0
            pointC = (pointB[0] + i*vecAB[0], pointB[1] + i*vecAB[1])
            while   pointC[0] >= 0 and pointC[0] < X and\
                    pointC[1] >= 0 and pointC[1] < Y:
                # print(pointC)
                antinodes[pointC[1]][pointC[0]] = "#"
                i+=1                
                pointC = (pointB[0] + i*vecAB[0], pointB[1] + i*vecAB[1])

            i = 0
            pointD = (pointA[0] + i*vecBA[0], pointA[1] + i*vecBA[1])
            while   pointD[0] >= 0 and pointD[0] < X and\
                    pointD[1] >= 0 and pointD[1] < Y:                        
                # print(pointD)
                antinodes[pointD[1]][pointD[0]] = "#"
                i+=1
                pointD = (pointA[0] + i*vecBA[0], pointA[1] + i*vecBA[1])


count = 0
for y in range(Y):
    for x in range(X):
        print(antinodes[y][x],end="")
        if antinodes[y][x] == "#": count += 1
    print()

print(count)