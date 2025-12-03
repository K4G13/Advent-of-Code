f = open("input.txt","r")
battery_banks = f.read().split()
f.close()

def largest_2_joltage(bank: str) -> int:
    max_jol = 0
    for idx1 in range(len(bank)):
        for idx2 in range(idx1+1,len(bank)):
            jol = int(bank[idx1]+bank[idx2])
            if jol > max_jol: max_jol = jol
    return max_jol

def largest_12_joltage(bank: str) -> int:

jol_sum = 0
for bank in battery_banks:
    res = largest_2_joltage(bank)
    jol_sum += res
    # print(res)
print(jol_sum)