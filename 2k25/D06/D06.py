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
