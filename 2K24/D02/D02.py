f = open("input")
raw_data = f.read()
f.close()

reports = raw_data.split("\n")

def safe(arr):

    prv_sign = None

    for i in range(1,len(arr)):

        diff = arr[i] - arr[i-1]
        if diff == 0: 
            return False

        if prv_sign == None: 
            prv_sign = 1 if diff > 0 else -1
        sign = 1 if diff > 0 else -1
        if sign != prv_sign:
            return False
        
        prv_sign = sign

        if abs(diff) < 1 or abs(diff) > 3: 
            return False
        
    return True

def safe_sub1(arr):

    for i in range(len(arr)):
        if safe(arr[:i] + arr[i+1:]): return True 

    return False

counter = 0
for el in reports:
    arr = list(map(int,el.split(" ")))
    if safe(arr): 
        counter += 1
print(counter)

# PART 2

counter = 0
for el in reports:
    arr = list(map(int,el.split(" ")))
    if safe_sub1(arr): 
        counter += 1
print(counter)