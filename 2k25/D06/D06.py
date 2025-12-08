def parse(string):
    splited = string.split()
    intList = list(map(int,splited))
    return intList

rawRows = open("input","r").read().split("\n")
numerRows = list(map(parse,rawRows[:-1]))
operations = rawRows[-1].split()

# PART 01
grandTotal = 0
for i,op in enumerate(operations):
    result = 1 if op == "*" else 0
    for row in numerRows:
        if op == "*": result *= row[i]
        if op == "+": result += row[i]
    grandTotal += result

print(grandTotal)

# PART 02
import numpy as np 
rawRows = open("input","r").read().split("\n")
operators = rawRows[-1].split()
M = np.array(list(map(list,rawRows[:-1])))
M = np.rot90(M)

grandTotal = 0
partialTotal = 0
opIdx = len(operators) - 1
for row in M:

    s = "".join(row).strip(" ")
    if s == "": 
        opIdx -= 1
        grandTotal += partialTotal
        partialTotal = 1 if operators[opIdx] == "*" else 0
        continue

    number = int(s)

    if operators[opIdx] == "*": partialTotal *= number
    if operators[opIdx] == "+": partialTotal += number
grandTotal += partialTotal

print(grandTotal)