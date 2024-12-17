import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--draw', action='store_true')
parser.add_argument('-p', '--pause', action='store_true')
parser.add_argument('-f', '--file', default='input')
args = parser.parse_args()

def load_data():
    
    data = open(args.file).read().split('\n')

    matrix = []
    instructions = []

    offset = 0
    for i,row in enumerate(data):

        if row == "":
            offset = i
            break

        matrix.append(list(row))

    for row in data[offset+1:]:
        instructions.extend(list(row))

    return matrix,instructions

def draw(matrix,sep=" "):
    
    for row in matrix:
        for el in row:
            print(el,end=sep)
        print()

    if args.pause: input()

class Bot:

    def __init__(self,mtrx):
        self.mtrx = mtrx        
        self.x = 0
        self.y = 0
        self.find_start()

    def find_start(self):
        for y, row in enumerate(self.mtrx):
            for x, el in enumerate(row):
                if el == "@": self.x, self.y = x, y

    def move(self,inst):

        dx,dy = 0,0
        if inst == '>': dx = +1
        if inst == '<': dx = -1
        if inst == 'v': dy = +1
        if inst == '^': dy = -1

        if self.mtrx[self.y+dy][self.x+dx] == '.':
            self.x += dx
            self.y += dy
            self.mtrx[self.y][self.x] = '@'
            self.mtrx[self.y-dy][self.x-dx] = '.'

        elif self.mtrx[self.y+dy][self.x+dx] == 'O':
            if self.push(self.x+dx,self.y+dy,dx,dy):                
                self.x += dx
                self.y += dy
                self.mtrx[self.y][self.x] = '@'
                self.mtrx[self.y-dy][self.x-dx] = '.'

    def push(self,x,y,dx,dy):
        
        if self.mtrx[y+dy][x+dx] == 'O':
            is_space = self.push(x+dx,y+dy,dx,dy)
            if is_space:
                self.mtrx[y+dy][x+dx] = 'O'
                return True
            else:
                return False

        if self.mtrx[y+dy][x+dx] == '.':
            self.mtrx[y+dy][x+dx] = 'O'
            return True
        
        if self.mtrx[y+dy][x+dx] == '#':
            return False

        return False

    def calc_GPS(self):
        total = 0
        for y,row in enumerate(self.mtrx):
            for x,el in enumerate(row):
                if el == "O": 
                    total += 100*y + x
        return total


# simulate PART 1
mtrx,instructions = load_data()
bot = Bot(mtrx)

for inst in instructions:
    bot.move(inst)
    if args.draw: 
        print("Inst:",inst)
        draw(bot.mtrx)
print(f"[ PART 1 ] GPS = {bot.calc_GPS()}")
