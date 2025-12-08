import numpy as np

rows = open("input", "r").read().split("\n")
Matrix = np.array(list(map(list,rows[:-1])))
operators = rows[-1].split()

# PART 01
grandTotal = 0
for i,op in enumerate(operators):
    total = 0 if op == "+" else 1
    for row in Matrix:
        number = int("".join(row).split()[i])
        if op == "+": total += number
        if op == "*": total *= number
    grandTotal += total
print(grandTotal)

# PART 02
Matrix = np.rot90(Matrix)
opIdx = len(operators)-1
grandTotal = 0
total = 0 if operators[opIdx] == "+" else 1
for row in Matrix:
    s = "".join(row).strip(" ")
    if not s:
        opIdx -= 1
        grandTotal += total
        total = 0 if operators[opIdx] == "+" else 1
        continue
    number = int(s)
    if operators[opIdx] == "+": total += number
    if operators[opIdx] == "*": total *= number
grandTotal += total
print(grandTotal)
