grid = [list(line) for line in open("input").read().split("\n")]

def dijkstra(start,grid):

    print("Initializing dijkstra...")

    visited = [ [False]*(len(grid)) for _ in range(len(grid[0])) ]

    Vertices = {} # (x,y): (distance, previous)
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == '#': visited[y][x] = True
            else: Vertices[(x,y)] = (float('inf'),None)

    Vertices[start] = (0,None)

    progress = 0

    while True:

        progress += 1
        percentage = (progress-1)*100/len(Vertices)
        bars = int(percentage//10)
        print(f"[{'='*bars}{' '*(10-bars)}] {(percentage):5.2f}%",end="\r")

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

    print()
    return Vertices

start,end = (0,0),(0,0)
for y,row in enumerate(grid):
    for x,c in enumerate(row):
        if c == 'S': start = (x,y)
        if c == 'E': end = (x,y)

grid_dist = dijkstra(start,grid)

path = []
curr = end
while curr != None:
    path.append(curr)
    curr = grid_dist[curr][1]
path = path[::-1]

def lurke(start,range):
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c != '#' and abs(start[0] - x) + abs(start[1] - y) <= range:
                yield (x,y)


# PART1

cheats_times = {}
print(f"Cheking cheats with 2 picoseconds...")
for progress,cheat_start in enumerate(path):

    percentage = (progress+1)*100/len(path)
    bars = int(percentage//10)
    print(f"[{'='*bars}{' '*(10-bars)}] {(percentage):5.2f}%",end="\r")
    
    for cheat_end in lurke(cheat_start,2):
        if cheat_end not in path: continue
        if grid_dist[cheat_start][0] <= grid_dist[cheat_end][0]: continue 

        time_saved = grid_dist[cheat_start][0] - grid_dist[cheat_end][0] - 2

        if time_saved > 0:
            if time_saved in cheats_times: cheats_times[time_saved] += 1
            else: cheats_times[time_saved] = 1
print()        

count = 0
for time,amount in cheats_times.items():
    if time >= 100: count += amount
print("[PART1]",count)


# PART2

cheats_times = {}
print(f"Cheking cheats with up to 20 picoseconds...")
for progress,cheat_start in enumerate(path):

    percentage = (progress+1)*100/len(path)
    bars = int(percentage//10)
    print(f"[{'='*bars}{' '*(10-bars)}] {(percentage):5.2f}%",end="\r")
    
    for cheat_end in lurke(cheat_start,20):
        if cheat_end not in path: continue
        if grid_dist[cheat_start][0] >= grid_dist[cheat_end][0]: continue 

        cheat_time = abs(cheat_start[0]-cheat_end[0]) + abs(cheat_start[1]-cheat_end[1])
        time_saved = grid_dist[cheat_end][0] - grid_dist[cheat_start][0] - cheat_time

        if time_saved > 0:
            if time_saved in cheats_times: cheats_times[time_saved] += 1
            else: cheats_times[time_saved] = 1

print()        

count = 0
for time,amount in cheats_times.items():
    if time >= 100: 
        count += amount        
print("[PART2]",count)
