f = open("input")
raw_data = f.read().split("\n")
f.close()

rules,updates = [],[]
for el in raw_data:
    if el.count("|"): rules.append(el)
    else: updates.append(el.split(","))
updates = updates[1:]


def list_restricted(value):
    res = []
    for rule in rules:
        k,v = rule.split("|")
        if v == value: res.append(k)
    return res

def check_update(update):
    for i in range(0,len(update)):
        restricted = list_restricted(update[i])
        for el in update[i+1:]:
            if el in restricted:
                # print(f"(!) RULE: {el}|{update[i]}")
                return False
    return True

count_sum = 0
for u in updates:
    if check_update(u): count_sum += int(u[len(u)//2])
print(count_sum)