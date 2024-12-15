import copy

f = open("input")
raw_data = f.read().split("\n")
f.close()

og_map = []
for row in raw_data: og_map.append(list(row))
X,Y = len(og_map[0]),len(og_map)
guard_spawn = (None,None)
for y in range(Y):
    for x in range(X):
        if og_map[y][x] == "^":
            guardSpawn = (x,y)
            og_map[y][x] = "."


def printMap(map):
    for row in map:
        for el in row:
            print(el,end=" ")
        print()

def simulate( m=copy.deepcopy(og_map), return_path=False, p=False ):

    x,y = guardSpawn
    dx,dy = 0,-1
    visited = set()

    while True:
        
        m[y][x] = "X"

        if p:
            print()
            printMap(m)
            input()

        if (x,y,dx,dy) in visited: return False
        visited.add((x,y,dx,dy))

        if x+dx < 0 or x+dx >= X or y+dy < 0 or y+dy >= Y: 
            if return_path: 
                path = []
                for y in range(Y):
                    for x in range(X):
                        if m[y][x] == "X": path.append((x,y))
                return path
            else: return True

        if m[y+dy][x+dx] == "#" or m[y+dy][x+dx] == "O":
            if dy == -1: dx,dy = 1,0
            elif dx == 1: dx,dy = 0,1
            elif dy == 1: dx,dy = -1,0
            elif dx == -1: dx,dy = 0,-1

        else:
            x += dx
            y += dy   


# PART 1

new_map = copy.deepcopy(og_map)
path = simulate(new_map,return_path=True)
count = 0
for row in new_map:
    count += row.count("X")
print(count)

# PART 2

count = 0

load = 0
loadMax = len(path)

for obsticle in path[1:]:

    load += 1
    chunks = 20
    print("[","="*((load+1)*chunks//loadMax)," "*(chunks - (load+1)*chunks//loadMax),"]",f" {((load+1)/loadMax*100):5.2f}%",sep="",end= "\r")

    new_map = copy.deepcopy(og_map)
    new_map[obsticle[1]][obsticle[0]] = "O"
    res = simulate(new_map)
    if res == False: 
        count += 1
print(" "*100,end="\r")
print(count)
