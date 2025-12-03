f = open("input.txt","r")
batteryBanks = f.read().split()
f.close()

def largestJoltage(length: int, bank: str) -> int:

    # print(bank)

    unique = set()
    unique.update(bank)
    uniqueSorted = list(unique)
    uniqueSorted.sort(reverse=True)

    # print(uniqueSorted)

    validIdxes = []

    for maxChar in uniqueSorted:
        for idx in range(len(bank)):
            if bank[idx] == maxChar and idx + length <= len(bank): 
                validIdxes.append(idx)
        if validIdxes: break
    
    # print(validIdxes)

    if length == 1: return bank[validIdxes[0]]

    maxReturned = 0
    for idx in validIdxes:
        res = largestJoltage(length-1,bank[idx+1:])
        if int(res) > maxReturned: maxReturned = int(res)

    return str(bank[validIdxes[0]]) + str(maxReturned)

sumOf2 = 0
sumOf12 = 0
for bank in batteryBanks:
    sumOf2 += int(largestJoltage(2,bank))
    sumOf12 += int(largestJoltage(12,bank))

print(sumOf2)
print(sumOf12)
