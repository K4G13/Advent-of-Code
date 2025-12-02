# 18700015741
# 20077272987

f = open("input.txt", "r")
idRanges = f.read().split(",")
f.close()

def isValidId(id: int) -> bool:
    idStr = str(id)
    l = len(idStr)
    part1 = idStr[:l//2]
    part2 = idStr[l//2:]
    return part1 == part2

def isValidId2(id: int) -> bool:
    idStr = str(id)
    length = len(idStr)
    deviders = []
    for i in range(1,length): 
        if length % i == 0: deviders.append(i)
    for window in deviders:
        parts = [idStr[j:j+window] for j in range(0, length, window)]
        all_equal = True
        for part in parts:
            if part != parts[0]: 
                all_equal = False
                break
        if all_equal: return True
    return False

sumValidIds = 0
sumValidIds2 = 0
for rangePair in idRanges:

    rangeStart, rangeEnd = map(int,rangePair.split("-"))
    for i in range(rangeStart, rangeEnd + 1):
        if isValidId(i): sumValidIds += i
        if isValidId2(i): sumValidIds2 += i

print(sumValidIds)
print(sumValidIds2)

