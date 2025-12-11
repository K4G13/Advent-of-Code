import re 

def parse(file: str):

    lines = open(file,"r").read().splitlines()
    machines = []

    for line in lines:

        machine = dict()

        machine["lights"] = re.findall("\\[(.*)\\]",line)[0]

        machine["switches"] = []
        switchesAll = re.findall("\\(([0-9,]*)\\)",line)
        for s in switchesAll:
            switches = list(map(int,s.split(',')))
            machine["switches"].append(switches)

        machine["jolts"] = list(map(int,re.findall("{(.*)}",line)[0].split(",")))

        machines.append(machine)

    return machines

def intToBinEncoding(n: int, lenght: int) -> int:
    # n=3 l=6
    # "000100" -> 0b100 -> 8
    s = f"{'0'*n}1{'0'*(lenght-n-1)}"
    return int(s,2)

machines = parse("input")

def minSwitches(lights: str, switchesList: list[list[int]]) -> int:

    minValue = 999999999

    NOLights = len(lights)
    NOSwitches = len(switchesList)

    lBin = int(lights.replace('.','0').replace('#','1'),2)
    # print(lights,bin(lBin),lBin,sep=" -> ")

    sBin = []
    for switches in switchesList:
        binValue = 0
        for s in switches:
            binValue ^= intToBinEncoding(s,len(lights))
        sBin.append(binValue)
    
    for combo in range(2**NOSwitches):

        comboBin = f"{bin(combo)[2:]:0>{NOSwitches}}"
        switchIdxes = [i for i, c in enumerate(comboBin) if c == "1"]


        xorTotal = 0
        for sIdx in switchIdxes:
            xorTotal ^= sBin[sIdx]

        lightsOutput = f"{bin(xorTotal)[2:]:0>{NOLights}}"

        # print(combo,"\t",comboBin,lightsOutput,end=" ")
        # if xorTotal == lBin: print("YEEEEEEEEEE!")

        if xorTotal == lBin:
            minValue = min(minValue,comboBin.count("1"))

    return minValue

total = 0
for m in machines:
    total += minSwitches(m["lights"],m["switches"])
print(total)