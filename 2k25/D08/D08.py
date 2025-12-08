import numpy as np

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): return f"<{self.x},{self.y},{self.z}>"
    def __repr__(self): return f"<{self.x},{self.y},{self.z}>"

def parseInput(filePath: str) -> list[Point]:
    rawLines = open(filePath,"r").read().split("\n")
    points = []
    for row in rawLines:
        x,y,z = list(map(int,row.split(",")))
        points.append(Point(x,y,z))
    return points

def dist(A: Point, B: Point) -> float:
    xSqr = (A.x - B.x)**2
    ySqr = (A.y - B.y)**2
    zSqr = (A.z - B.z)**2
    return np.sqrt(xSqr+ySqr+zSqr)

def getNClosest(points: list[Point], N: int) -> list[float,Point,Point]:

    distances = []
    for idx1 in range(len(points)):
        for idx2 in range(idx1):
            A,B = points[idx1],points[idx2]
            distances.append( (dist(A,B), B, A) ) 

    distances.sort(key=lambda x: x[0] )

    return distances[:N]

points = parseInput("input")
closest = getNClosest(points,1000)
circuits = []

for d,A,B in closest:

    flagA, flagB = False, False
    idxA, idxB = None, None

    for i,c in enumerate(circuits):
        if A in c:
            flagA = True
            idxA = i
        if B in c:
            flagB = True
            idxB = i

    if not flagA and not flagB: circuits.append([A,B]) 
    if flagA and not flagB: circuits[idxA].append(B)
    if not flagA and flagB: circuits[idxB].append(A)
    if flagA and flagB and idxA != idxB:
        circuits[idxA] += circuits[idxB]
        circuits.pop(idxB)

circuitsLengths = list(map(len,circuits))
circuitsLengths.sort(reverse=True)

print( circuitsLengths[0]*circuitsLengths[1]*circuitsLengths[2] )