raw_input  = open("input").read()
topography = [list(map(int,x)) for x in raw_input.split("\n")]

NR,NC = len(topography),len(topography[0])

starts = []
for y in range(NR):
    for x in range(NC):
        if topography[y][x] == 0:
            starts.append((x,y))

def find_endpoints(x,y,h=0):

    endpoints = set()

    if h==9: return {(x,y)}

    if x > 0 and topography[y][x-1] == h+1:
        endpoints.update( find_endpoints(x-1,y,h+1) )
    
    if x < NC-1 and topography[y][x+1] == h+1:
        endpoints.update( find_endpoints(x+1,y,h+1) )

    if y > 0 and topography[y-1][x] == h+1:
        endpoints.update( find_endpoints(x,y-1,h+1) )

    if y < NR-1 and topography[y+1][x] == h+1:
        endpoints.update( find_endpoints(x,y+1,h+1) )

    return endpoints

count = 0
for start in starts:
    x,y = start
    endpoints = find_endpoints(x,y)
    count += len(endpoints)

print(count)

# PART 2

def find_paths(x,y,h=0):

    if h==9: return 1

    score = 0

    if x > 0 and topography[y][x-1] == h+1:
        score += find_paths(x-1,y,h+1) 
    
    if x < NC-1 and topography[y][x+1] == h+1:
        score += find_paths(x+1,y,h+1) 

    if y > 0 and topography[y-1][x] == h+1:
        score += find_paths(x,y-1,h+1) 

    if y < NR-1 and topography[y+1][x] == h+1:
        score += find_paths(x,y+1,h+1) 

    return score

count = 0
for start in starts:
    x,y = start
    count += find_paths(x,y)
print(count)