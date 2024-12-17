import re

ROWS = 103 #103
COLS = 101 #101
SIMULATION_TIME = 100
DRAW = False
PAUSE = False

raw_data   = open("input").read().split('\n')
behaviours = [ list(map(int,re.findall(r'-?\d+',x))) for x in raw_data ]
positions  = [ [x[0],x[1]] for x in behaviours ]

def draw_state(quadrants=False,iteration=0):

    print("Iteration: ",iteration)

    for y in range(ROWS):

        for x in range(COLS):
            
            count = positions.count([x,y])
            char  = "."
            
            if quadrants and (x==COLS//2 or y==ROWS//2): char = "."
            if count != 0: char = count

            print(char,end=" ")

        print()   

    if PAUSE: input()
    print("\033[A"*(ROWS+2), end='')  



if DRAW: draw_state(True)

#simulate movement
for iteration in range(SIMULATION_TIME):

    for i,pos in enumerate(positions):
        x,y = pos
        dx,dy = behaviours[i][2:]
        x = (x+dx)%COLS
        y = (y+dy)%ROWS
        positions[i] = [x,y]

    if DRAW: draw_state(True,iteration)
if DRAW: print("\n"*ROWS)

#count quadrants
q1,q2,q3,q4 = 0,0,0,0
for p in positions:
    x,y = p
    if x < COLS//2 and y < ROWS//2: q1 += 1
    if x > COLS//2 and y < ROWS//2: q2 += 1
    if x < COLS//2 and y > ROWS//2: q3 += 1
    if x > COLS//2 and y > ROWS//2: q4 += 1
safety_factor = q1*q2*q3*q4
print("PART1: ",safety_factor)


# PART 2 hunt for easteregg
# 7138 G
MIN_INROW = 8
positions  = [ [x[0],x[1]] for x in behaviours ]

iteration = 0
while iteration>=0:

    iteration+=1

    print("Iteration: ",iteration,end="\r")

    matrix = [ [False]*COLS for _ in range(ROWS) ]

    for i,pos in enumerate(positions):
        x,y = pos
        dx,dy = behaviours[i][2:]
        x = (x+dx)%COLS
        y = (y+dy)%ROWS
        positions[i] = [x,y]
        matrix[y][x] = True

    found = False
    for y in range(ROWS):
        inrow = 0
        if found: break
        for x in range(COLS):

            if matrix[y][x]: inrow += 1
            else: inrow = 0

            if inrow >= MIN_INROW:
                

                for row in matrix:
                    for el in row:
                        if el: print("#",end=" ")
                        else:  print(".",end=" ")
                    print()
                
                print("Iteration: ",iteration)
                input()
                found = True
                break
                




