f = open("input.txt","r")
batteryBanks = f.read().split()
f.close()

def largestJoltage(length: int, bank: str) -> int:

    unique = set()
    unique.update(bank)
    uniqueSorted = list(unique)
    uniqueSorted.sort(reverse=True)

    validIdxes = []
    for maxChar in uniqueSorted:
        for idx in range(len(bank)):
            if bank[idx] == maxChar and idx + length <= len(bank): 
                validIdxes.append(idx)
        if validIdxes: break

    if length == 1: return int(bank[validIdxes[0]])

    maxReturned = 0
    for idx in validIdxes:
        res = largestJoltage(length-1,bank[idx+1:])
        maxReturned = max(maxReturned,res)

    return int(str(bank[validIdxes[0]]) + str(maxReturned))

sumOf2 = 0
sumOf12 = 0
for bank in batteryBanks:
    sumOf2 += largestJoltage(2,bank)
    sumOf12 += largestJoltage(12,bank)

print(sumOf2)
print(sumOf12)
