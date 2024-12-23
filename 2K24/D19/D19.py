import re

f = open("input")
TOWELS = re.findall(r'[a-z]+',f.readline())
f.readline()
PATTERNS = f.read().split("\n")

cashe = {}
def recursive(pattern):

    global TOWELS

    if pattern in cashe: return cashe[pattern]

    if pattern == "": return 1

    total = 0
    for i in range(len(pattern)):
        
        subpatern = pattern[:i+1]

        if subpatern in TOWELS:
            res = recursive(pattern[i+1:])
            if res > 0: total += res

    cashe[pattern] = total
    return total


count_possible = 0
sum_possible = 0
for i,p in enumerate(PATTERNS):
    res = recursive(p)
    if res: 
        count_possible += 1
        sum_possible += res
#PART 1
print(count_possible)
#PART 2
print(sum_possible)
