INPUT_NAME = "input"
DRAW = False
PAUSE = False

def load_input(file_name):
    raw_input = open(file_name).read().split("\n")

    warehouse = []
    moves = []

    offset = 0
    for i,row in enumerate(raw_input):
        if row == "":
            offset = i
            break
        warehouse.append(list(row))
    for row in raw_input[offset+1:]:
        moves.extend(list(row))

    return warehouse,moves

class Bot:
    def __init__(self):
        self.x = 0
        self.y = 0

def draw():
    for row in warehouse:
        for el in row:
            print(el,end=" ")
        print()

def push(x,y,dx,dy):

    count = 0

    if warehouse[ y+dy ][ x+dx ] == ".":
        warehouse[ y+dy ][ x+dx ] = "O"
        return 1
    
    elif warehouse[ y+dy ][ x+dx ] == "O":
        count += push(x+dx,y+dy,dx,dy)        

    elif warehouse[ y+dy ][ x+dx ] == "#":
        return count

    return count

warehouse,moves = load_input(INPUT_NAME)
ROWS = len(warehouse)
COLS = len(warehouse[0])
bot = Bot
for y,row in enumerate(warehouse):
    for x,el in enumerate(row):
        if el == "@": 
            bot.x = x
            bot.y = y

if DRAW:
    print("Initial state:")
    draw()
if PAUSE: input()
if DRAW and not PAUSE: print()

#simulate
for move in moves:
    
    dx,dy = 0,0

    if (move == ">"): dx += 1
    if (move == "<"): dx -= 1
    if (move == "v"): dy +=1
    if (move == "^"): dy -= 1


    if warehouse[ bot.y+dy ][ bot.x+dx ] == ".":
        warehouse[ bot.y ][ bot.x ] = "."
        bot.x += dx
        bot.y += dy
        warehouse[ bot.y ][ bot.x ] = "@"
    
    elif warehouse[ bot.y+dy ][ bot.x+dx ] == "#":
        ...
    
    elif warehouse[ bot.y+dy ][ bot.x+dx ] == "O":
        if push( bot.x+dx, bot.y+dy, dx, dy ) > 0: 
            warehouse[ bot.y ][ bot.x ] = "."
            bot.x += dx
            bot.y += dy
            warehouse[ bot.y ][ bot.x ] = "@"

    if DRAW:         
        print(f"Move {move}:")
        draw()
    if PAUSE: input()
    if DRAW and not PAUSE: print()

#sum GPS coordinates
total = 0
for y,row in enumerate(warehouse):
    for x,el in enumerate(row):
        if el == "O": total += 100*y + x
print(f"[PART1] Sum of GPS coordinates: {total}")
