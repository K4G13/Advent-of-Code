maze = [ list(line) for line in open("input").read().split('\n')]
visited = [ [False]*len(maze[0]) for _ in range(len(maze))]
dijkstra = {} # (x,y): (distance, previous, direction)

for y,row in enumerate(maze):
    for x,c in enumerate(row):
        if c == "#": visited[y][x] = True
        elif c == "S": dijkstra[ (x,y) ] = (0,None,"HORIZONTAL") 
        else: dijkstra[ (x,y) ] = (float('inf'),None,None)

NVertices = len(dijkstra)
iteration = 0

while True:

    print( f"[PART1]: [{'='*(iteration*10//NVertices)}{' '*(10-iteration*10//NVertices)}] {iteration*100/NVertices:2.2f}%", end="\r")
    iteration += 1

    # find not visited node with smallest distance
    v = None
    for y,row in enumerate(maze):
        for x,c in enumerate(row):
            if not visited[y][x]:
                if v == None or dijkstra[(x,y)][0] < dijkstra[v][0]:
                    v = (x,y)

    # exit if all nodes are visited
    if v == None: break

    neighbors = []
    x,y = v
    # mark curr v as visited
    visited[y][x] = True
    # add neighbors of current v with relation
    if not visited[y][x-1]: neighbors.append( (x-1,y,"HORIZONTAL") )
    if not visited[y][x+1]: neighbors.append( (x+1,y,"HORIZONTAL") )
    if not visited[y+1][x]: neighbors.append( (x,y+1,"VERTICAL"  ) )
    if not visited[y-1][x]: neighbors.append( (x,y-1,"VERTICAL"  ) )

    # update neighbors
    for x,y,relation in neighbors:
        cost = 1 if dijkstra[v][2] == relation else 1001
        if dijkstra[(x,y)][0] > dijkstra[v][0] + cost:
            dijkstra[(x,y)] = ( dijkstra[v][0] + cost, v, relation ) 

path = []
for y,row in enumerate(maze):
    for x,c in enumerate(row):
        if c == "E":

            el = (x,y)
            while el != None:
                path.append(el)
                el = dijkstra[el][1]

            print()
            print(dijkstra[(x,y)][0])
            break

# PART 2
