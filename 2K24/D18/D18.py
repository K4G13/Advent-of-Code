import time

# 6 for test, 70 for input
SIZE = 70
# 12 for test, 1024 for input
SIM_ITER = 1024
FILE = "input"
PRINT = True
SLEEP_T = 0

raining_bytes = [ tuple(map(int,line.split(","))) for line in open(FILE).read().split("\n")]

grid = [['.' for _ in range(SIZE+1)] for _ in range(SIZE+1)]

def simulate(iterations=1):
    last_dropped = None
    for _ in range(iterations):
        x,y = raining_bytes.pop(0)
        last_dropped = (x,y)
        grid[y][x] = '#'
    return last_dropped
        

def dijkstra(start,grid):

    visited = [ [False]*(SIZE+1) for _ in range(SIZE+1) ]

    Vertices = {} # (x,y): (distance, previous)
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == '#': visited[y][x] = True
            else: Vertices[(x,y)] = (float('inf'),None)

    Vertices[start] = (0,None)

    while True:

        v = None

        for y,row in enumerate(grid):
            for x,c in enumerate(row):
                if not visited[y][x]:
                    if v == None or Vertices[(x,y)][0] < Vertices[v][0]:
                        v = (x,y)

        if v == None: break

        neighbors = []

        x,y = v
        visited[y][x] = True
        if (x-1,y) in Vertices and not visited[y][x-1]: neighbors.append( (x-1,y) )
        if (x+1,y) in Vertices and not visited[y][x+1]: neighbors.append( (x+1,y) )
        if (x,y-1) in Vertices and not visited[y-1][x]: neighbors.append( (x,y-1) )
        if (x,y+1) in Vertices and not visited[y+1][x]: neighbors.append( (x,y+1) )

        for n in neighbors:
            if Vertices[n][0] > Vertices[v][0] + 1:
                Vertices[n] = ( Vertices[v][0] + 1, v )


    path = [(SIZE,SIZE)]
    curr = Vertices[(SIZE,SIZE)][1]
    while curr != None:
        path.append( curr )
        curr = Vertices[curr][1]

    return path[::-1]

# PART 1
simulate(SIM_ITER)
path = dijkstra((0,0),grid)
print(len(path)-1)

# PART 2
last_byte=None
while len(path) > 1:

    while last_byte not in path:
        last_byte = simulate()

    path = dijkstra((0,0),grid)

    if PRINT:
        for x,y in path:
            grid[y][x] = 'O'
        for row in grid:
            print(" ".join(row))
        for x,y in path:
            grid[y][x] = '.'
        print("\033[A"*(SIZE+2))
        time.sleep(SLEEP_T)

if PRINT: print("\n"*(SIZE))

print(last_byte)