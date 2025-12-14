FILE = "input"

import numpy as np

def getShapes(fileName):

    rawShapes = open(fileName,"r").read().split("\n\n")[:-1]
    # print(rawShapes)

    rawShapes = list(map(lambda x: x.split(":")[1],rawShapes))
    # print(rawShapes)

    rawShapes = [row.replace("#","1").replace(".","0") for row in rawShapes]
    # print(rawShapes)

    rawShapes = [ [list(map(int,s)) for s in shape.split()] for shape in rawShapes ]
    # print(rawShapes)

    shapes = []
    for idx,matrix in enumerate(rawShapes):
        shape = {}
        shape["idx"] = idx
        
        var1 = np.array(matrix)
        var2 = np.rot90(var1)
        var3 = np.rot90(var2)
        var4 = np.rot90(var3)

        dec1 = [ int(''.join(map(str, row.flatten())),2) for row in var1 ]
        dec2 = [ int(''.join(map(str, row.flatten())),2) for row in var2 ]
        dec3 = [ int(''.join(map(str, row.flatten())),2) for row in var3 ]
        dec4 = [ int(''.join(map(str, row.flatten())),2) for row in var4 ]

        # shape["bin"] = [var1,var2,var3,var4]
        shape["dec"] = [dec1,dec2,dec3,dec4]

        shape["area"] = sum([sum(row) for row in matrix])
        
        shapes.append(shape)

    return shapes

def getRegions(fileName):
    rawRegions = open(fileName,"r").read().split("\n\n")[-1].splitlines()

    regions = []
    for line in rawRegions:
        spitted = line.split(":")
        width, height = list(map(int,spitted[0].split("x")))
        idxes = list(map(int,spitted[1].split()))
        regions.append({"width": width, "height": height, "indexes": idxes})

    return regions

SHAPES = getShapes(FILE)
REGIONS = getRegions(FILE)

def checkUpperBound():

    count = 0
    for r in REGIONS:
        
        totalPresentsArea = 0
        for idx,amount in enumerate(r["indexes"]):
            totalPresentsArea += SHAPES[idx]["area"]*amount
        
        if totalPresentsArea < r["height"]*r["width"]: count += 1

    print("Upper bound =",count)

checkUpperBound()