f = open("input")
equations = f.read().split("\n")
f.close()


def evaluate(numbers,resolution):

    if len(numbers) == 1:
        if resolution == numbers[0]: return True
        else: return False

    adding = evaluate(numbers[:-1],resolution-numbers[-1])
    multiplying = evaluate(numbers[:-1],resolution/numbers[-1])
    return adding or multiplying


count_sum = 0
for equation in equations:

    resolution,nummbers = equation.split(": ")
    resolution = int(resolution)
    nummbers = nummbers.split(" ")
    nummbers = [int(x) for x in nummbers]

    correct = evaluate(nummbers,resolution)
    if correct: count_sum += resolution

print(count_sum)


# PART 2



    
