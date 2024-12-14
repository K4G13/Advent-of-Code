f = open("input")
raw_data = f.read().split("\n")
f.close()

# number of columns and rows
NC,NR = len(raw_data[0]),len(raw_data)

visited = [[False for _ in range(NC)] for _ in range(NR)]
def print_visited():
    for y in range(NR):
        for x in range(NC):
            if visited[y][x]: print("X",end="")
            else: print(".",end="")
            if raw_data[y][x] == "#": print("#",end="")
        print()

# find the guard
guard = (None,None)
dx = 0
dy = -1
for y in range(NR):
    for x in range(NC):
        if raw_data[y][x] == "^":
            guard = (x,y)
            visited[y][x] = True
            break

while True:
    x,y = guard
    visited[y][x] = True

    if y+dy < 0 or y+dy >= NR or x+dx < 0 or x+dx >= NC: break
    if raw_data[y+dy][x+dx] == "#":
        if   dy == -1:  dx,dy = 1,0
        elif dx ==  1:  dx,dy = 0,1
        elif dy ==  1:  dx,dy = -1,0
        elif dx == -1:  dx,dy = 0,-1
    
    guard = (x+dx,y+dy)

count = 0
for row in visited:
    count += row.count(True)
print_visited()
print(count)
    