import re

f = open("input")
raw_data = f.read()
f.close()

clean_data = re.findall(r"mul\(\d{1,3},\d{1,3}\)",raw_data)

res = 0
for el in clean_data:
    a,b = re.findall(r"\d{1,3}",el)
    res += int(a) * int(b)
print(res)


# PART 2

clean_bonus_data = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",raw_data)

res = 0
enabled = True
for el in clean_bonus_data:
    
    if      el == "do()":       enabled = True
    elif    el == "don't()":    enabled = False
    else:
        a,b = re.findall(r"\d{1,3}",el)
        if enabled:
            res += int(a) * int(b)
            
print(res)