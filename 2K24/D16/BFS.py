import numpy as np

maze = np.matrix([ list(line) for line in open("input").read().split('\n')])

def find_start():
    for y in range(maze.shape[0]):
        for x in range(maze.shape[1]):
            if maze[y,x] == 'S': return x,y

def find_end(x,y,dir=(1,0),path=[],score=0):

    visited = np.full(maze.shape, False, dtype=bool)
    visited[y,x] = True
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if maze[i,j] == '#': visited[i,j] = True
    for p in path:
        visited[p[1],p[0]] = True

    if maze[y,x] == 'E':
        print('Found it!',score)
        return score

    possible_moves = []

    dx,dy = dir
    if not visited[y+dy,x+dx]:
        possible_moves.append((x+dx,y+dy,(dx,dy),score+1))

    if dx in [-1,1] and not visited[y-1,x]:
        possible_moves.append((x,y-1,(0,-1),score+1001))

    if dx in [-1,1] and not visited[y+1,x]:
        possible_moves.append((x,y+1,(0,1),score+1001))

    if dy in [-1,1] and not visited[y,x-1]:
        possible_moves.append((x-1,y,(-1,0),score+1001))

    if dy in [-1,1] and not visited[y,x+1]:
        possible_moves.append((x+1,y,(1,0),score+1001))

    print((x,y),dir,score)

    for j in range(maze.shape[0]):
        for i in range(maze.shape[1]):
            if (i,j) in path: print("O",end=" ")
            elif maze[j,i] == '#': print("#",end=" ")
            else: print(".",end=" ")
        print()

    print("\033[A"*(maze.shape[0]+2))

    # print("can do: ",end="")
    # for nx,ny,ndir,nscore in possible_moves:
    #     print([nx,ny,nscore],end=" ")
    # print()
    # input()


    minimum = float('inf')
    for nx,ny,ndir,nscore in possible_moves:
        result = find_end(nx,ny,ndir,path+[(x,y)],nscore)
        if result<minimum: minimum = result
        # if result: return result

    return minimum

    

xs,ys = find_start()
min_score = find_end(xs,ys)
print(min_score)