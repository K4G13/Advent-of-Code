raw_input  = open("input").read()
garden = [list(x) for x in raw_input.split("\n")]
X,Y = len(garden[0]),len(garden)

def getSection(x,y,points=set()):
    
    if (x,y) in points: return points
    points.add((x,y))

    if x>0 and garden[y][x-1] == garden[y][x]:
        points.update( getSection(x-1,y,points.copy()) )

    if x<X-1 and garden[y][x+1] == garden[y][x]:
        points.update( getSection(x+1,y,points.copy()) )

    if y>0 and garden[y-1][x] == garden[y][x]:
        points.update( getSection(x,y-1,points.copy()) )

    if y<Y-1 and garden[y+1][x] == garden[y][x]:
        points.update( getSection(x,y+1,points.copy()) )
    
    return points

def drawSection(points):
    x,y = list(points)[0]
    char = garden[y][x]
    print(f"\nArea for {char}:")

    for y in range(Y):
        for x in range(X):
            if (x,y) in points:
                print(char,end="")
            else:
                print(".",end="")
        print()

def getCircumference(points):
    circumference = 0
    for x,y in points:
        edges = 0
        if (x-1,y) in points: edges += 1
        if (x+1,y) in points: edges += 1
        if (x,y-1) in points: edges += 1
        if (x,y+1) in points: edges += 1
        circumference += 4 - edges
    return circumference


price = 0
visited = [[False for _ in range(X)] for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        if visited[y][x]: continue

        section = getSection(x,y)
        for p in section: visited[p[1]][p[0]] = True

        price += len(section) * getCircumference(section)

        # drawSection(section)
        # print(f"Area = {len(section)}")
        # print(f"Circ = {getCircumference(section)}")
        # input()

        section.clear()
print(price)
