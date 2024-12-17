import re

raw_input = open("input").read().split("\n")

machines = []
for i,row in enumerate(raw_input):

    if i%4 == 0:
        bttA = list(map(int,re.findall(r"\+(\d+)",row)))
        machines.append([])
        machines[-1].append(bttA)

    if i%4 == 1:
        bttB = list(map(int,re.findall(r"\+(\d+)",row)))
        machines[-1].append(bttB)

    if i%4 == 2:
        prize = list(map(int,re.findall(r"\=(\d+)",row)))
        machines[-1].append(prize)

def calc(bttA,bttB,prize):

    X,Y   = prize
    Xa,Ya = bttA
    Xb,Yb = bttB

    n = (Y*Xb - Yb*X)/(Ya*Xb - Xa*Yb)
    m = (X - Xa*n)/Xb

    return n,m

total = 0
for machine in machines:
    a,b,p = machine
    A,B = calc(a,b,p)

    tokens = 0

    if  int(A)==A and int(B)==B and\
        A>=0 and B>=0 and\
        A<=100 and B<=100:
        tokens = A*3 + B*1

    # print(A,B,tokens)
    total += int(tokens)

print(total)

