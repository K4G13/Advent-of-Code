def load_input(file_name):
    f = open("input")
    registerA = int(f.readline().split(" ")[2])
    registerB = int(f.readline().split(" ")[2])
    registerC = int(f.readline().split(" ")[2])
    f.readline()
    program = list(map(int,f.readline().split(" ")[1].split(",")))
    f.close()
    return registerA,registerB,registerC,program

# register A, register B, register C, program
register_a,register_b,register_c,program = load_input("input")

def combo(n):
    if n>=0 and n<=3: return n
    elif n == 4: return register_a
    elif n == 5: return register_b
    elif n == 6: return register_c
    raise ValueError(f"invalid opcode: {n}")

# instruction pointer
p = 0
# program output
output = []
while p < len(program):

    opcode = program[p]
    operand = program[p+1]

    # adv - division
    if opcode == 0:
        result = register_a // 2**combo(operand)
        register_a = result
        p+=2
    
    # bxl - bitwise XOR
    if opcode == 1:
        res = register_b ^ operand
        register_b = res
        p+=2

    # bst - literal modulo 8
    if opcode == 2:
        res = combo(operand) % 8
        register_b = res & 0b111
        p+=2

    # jnz - nothing/jump
    if opcode == 3:
        if register_a != 0:
            p = operand
        else: 
            p+=2

    # bxc - bitwise XOR
    if opcode == 4:
        res = register_b ^ register_c
        register_b = res
        p+=2

    # out - combo modulo 8
    if opcode == 5:
        res = combo(operand) % 8
        # print(res)
        output.append(res)
        p+=2

    # bdv - adv but stores at register b
    if opcode == 6:
        result = register_a // 2**combo(operand)
        register_b = result
        p+=2

    # cdb - adv but stores at register c
    if opcode == 7:
        result = register_a // 2**combo(operand)
        register_c = result
        p+=2

# PART 1
string = ""
for el in output:
    string += str(el) + ","
string = string[:-1]
print(string)

# PART 2
def run(register_a):
    A = register_a
    # C = A & 0b111
    # B = C ^ 0b11
    B = (A & 0b111) ^ 0b11
    C = A >> B
    B = B ^ C
    # A = A >> 3
    B = B ^ 0b101
    return B & 0b111
    # loop if A!=0

possible = {0}
for i in range(len(program)):
    expected = program[-(i+1)]
    
    for A in possible.copy():
        possible.remove(A)
        A = A*8

        for n in range(0,8):
            output = run(A+n)
            if output == expected:
                possible.add(A+n)

print(min(possible))

