def parse(file: str) -> list[(int,int)]:
    
    def getTuple(s: str):
        x,y = s.split(",")
        return (int(x),int(y))
    
    tiles = open(file,"r").read().splitlines()
    tiles = list(map(getTuple,tiles))
    return tiles

tiles = parse("input")

# PART 1
maxSize = 0
for idx1 in range(len(tiles)):
    x1,y1 = tiles[idx1]
    for idx2 in range(idx1,len(tiles)):
        x2,y2 = tiles[idx2]
        size = (abs(x1-x2)+1)*(abs(y1-y2)+1)
        maxSize = max(maxSize,size)
print(maxSize)