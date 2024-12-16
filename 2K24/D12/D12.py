# 953738 Git

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
        neighbours = 0
        if (x-1,y) in points: neighbours += 1
        if (x+1,y) in points: neighbours += 1
        if (x,y-1) in points: neighbours += 1
        if (x,y+1) in points: neighbours += 1
        circumference += 4 - neighbours
    return circumference


def getEdges(points,log=False):

    if log: drawSection(points)

    total = 0

    for p in points:

        print_lines = 0

        if(log): print(f"FOR: \t{p}")
        print_lines += 1

        matrix = [[0 for _ in range(X)] for _ in range(Y)]
        for y in range(-1,2):
            for x in range(-1,2):
                if (p[0]+x,p[1]+y) in points:
                    matrix[y+1][x+1] = 1

        for y in range(3):
            if(log): print("\t",end="")
            for x in range(3):
                if matrix[y][x] == 1:
                    if(log): print("#",end=" ")
                else:
                    if(log): print(".",end=" ")
            if(log): print()
            print_lines += 1

        corrners = []     #corner        a-neigbour    b-neigbour
        corrners.append( ( matrix[0][0], matrix[1][0], matrix[0][1] ) )
        corrners.append( ( matrix[0][2], matrix[1][2], matrix[0][1] ) )
        corrners.append( ( matrix[2][2], matrix[1][2], matrix[2][1] ) )
        corrners.append( ( matrix[2][0], matrix[1][0], matrix[2][1] ) )

        if(log): print(corrners)
        print_lines+=1

        correct = [False,False,False,False]

        for i in range(4):
            c,v,h = corrners[i]
            if v+h==0 and c==0: correct[i] = True
            if v+h==2 and c==0: correct[i] = True

        if(log): print(correct)
        print_lines+=1

        total += correct.count(True)

        if(log): print(f"Correct: {correct.count(True)}")
        if(log): print(f"Total: {total}")
        print_lines+=2

        if(log): input()
        if(log): print("\033[A"*(print_lines+1), end='')

    if(log): print("\n"*(print_lines+1), end='')

    return total



# PART 1

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


# PART 2

price = 0
visited = [[False for _ in range(X)] for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        if visited[y][x]: continue
        section = getSection(x,y)
        for p in section: visited[p[1]][p[0]] = True
        price += len(section) * getEdges(section,True)
        section.clear()
print(price)
