tachyonManifold = open("input","r").read().split("\n")
tachyonManifold = list(map(list,tachyonManifold))

def printTachyonManifold():
    print("="*30)
    for row in tachyonManifold:
        for char in row:
            print(char,end="")
        print()

# PART 01
splits = 0
for y,row in enumerate(tachyonManifold):
    for x,char in enumerate(row):
        
        above = tachyonManifold[y-1][x] if y-1>=0 else None

        if char=="S": tachyonManifold[y+1][x] = "|" 
        if char=="^" and above=="|":
            tachyonManifold[y][x-1] = "|"
            tachyonManifold[y][x+1] = "|"
            splits += 1
        if char=="." and above=="|": tachyonManifold[y][x] = "|"
print(splits)

# PART 02
cached = dict()
def quantumTachyonManifold(beanIdx: int, rowIdx: int):

    if rowIdx >= len(tachyonManifold): return 1
    if (beanIdx,rowIdx) in cached: return cached[(beanIdx,rowIdx)]

    if tachyonManifold[rowIdx][beanIdx]=="^":
        world01 = quantumTachyonManifold(beanIdx-1,rowIdx+1)
        world02 = quantumTachyonManifold(beanIdx+1,rowIdx+1)
        if (beanIdx,rowIdx) not in cached: cached[(beanIdx,rowIdx)] = world01 + world02
        return world01 + world02
    else: return quantumTachyonManifold(beanIdx,rowIdx+1)

startBeanIdx = "".join(tachyonManifold[0]).find("S")
worldsCounted = quantumTachyonManifold(startBeanIdx,0)
print(worldsCounted)