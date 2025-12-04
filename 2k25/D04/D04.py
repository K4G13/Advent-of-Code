f = open("input.txt", "r")
diagram = f.read().splitlines()
f.close()

def countNeighbors(xPos: int,yPos: int)->int:
    count = 0
    for y in range(yPos-1, yPos+2):
        for x in range(xPos-1, xPos+2):
            if x == xPos and y == yPos: continue
            if y < 0 or y >= len(diagram): continue
            if x < 0 or x >= len(diagram[y]): continue
            if diagram[y][x] == '@': count += 1
    return count

movable = 0
for y in range(len(diagram)):
    for x in range(len(diagram[0])):
        if diagram[y][x] == '.': continue
        neighbors = countNeighbors(x,y)
        if neighbors < 4: movable += 1
print(movable)

removable = 0
changed = True
while changed:
    
    changed = False

    #phase 1: find removable
    toRemove = []
    for y in range(len(diagram)):
        for x in range(len(diagram[0])):
            if diagram[y][x] == '.': continue
            neighbors = countNeighbors(x,y)
            if neighbors < 4:
                toRemove.append((x,y))

    #phase 2: remove
    if toRemove: changed = True
    for (x,y) in toRemove:
        diagram[y] = diagram[y][:x] + '.' + diagram[y][x+1:]
        removable += 1
        
print(removable)