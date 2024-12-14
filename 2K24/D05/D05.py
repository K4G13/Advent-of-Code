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

# PART 2

incorrect = []
for u in updates: 
    if not check_update(u): incorrect.append(u)

def correct_order(update):
    d = {}
    for i in range(0,len(u)):
        restricted = list_restricted(u[i])
        count = 0
        for el in restricted:
            if el in u: count += 1
        d[u[i]] = count        
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    res = []
    for k,v in d.items():
        res.append(k)
    return res

count_sum = 0
for u in incorrect:
    correct = correct_order(u)
    count_sum += int(correct[len(correct)//2])
print(count_sum)