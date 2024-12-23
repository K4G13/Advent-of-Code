import re

f = open("input")
TOWELS = re.findall(r'[a-z]+',f.readline())
f.readline()
PATTERNS = f.read().split("\n")

cashe = {}
def recursive(pattern):

    global TOWELS

    if pattern in cashe: return cashe[pattern]

    if pattern == "": return True,[]

    for i in range(len(pattern)):
        
        subpatern = pattern[:i+1]

        if subpatern in TOWELS:
            res,arr = recursive(pattern[i+1:])
            if res == True:
                cashe[pattern] = True,[subpatern]+arr
                return True, [subpatern]+arr
            
    cashe[pattern] = False,[]
    return False,[]


count_possible = 0
for i,p in enumerate(PATTERNS):
    res,arr = recursive(p)
    if res: count_possible += 1
print(count_possible)
