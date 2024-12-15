f = open("input")
equations = f.read().split("\n")
f.close()


def eval(numbers,score,target):

    if numbers == []: 
        if score == target: return True
        else: return False

    return  eval(numbers[1:], score + numbers[0],target) or\
            eval(numbers[1:], score * numbers[0],target)


def eval2(numbers,score,target):

    if numbers == []: 
        if score == target: return True
        else: return False

    return  eval2(numbers[1:], score + numbers[0],target) or\
            eval2(numbers[1:], score * numbers[0],target) or\
            eval2(numbers[1:], int(str(score) + str(numbers[0])),target)
    


count = 0
count2 = 0
for equation in equations:


    target,nummbers = equation.split(": ")
    target = int(target)
    nummbers = nummbers.split(" ")
    nummbers = [int(x) for x in nummbers]

    correct = eval(nummbers,0,target)
    if correct: count += target

    correct2 = eval2(nummbers,0,target)
    if correct2: count2 += target

print(count)    
print(count2)    
