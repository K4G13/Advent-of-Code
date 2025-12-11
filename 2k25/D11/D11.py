def parseDevices(devicesList: list[str]) -> dict:
    devices = dict()
    for dStr in devicesList:
        name,outputs = dStr.split(":")
        devices[name] = outputs.split()
    return devices

devicesRaw = open("input","r").read().splitlines()
devices = parseDevices(devicesRaw)

# PART 1
def countOutputPaths(curr,devices):

    if curr == "out": return 1

    count = 0
    for next in devices[curr]:
        count += countOutputPaths(next,devices)    
    return count

print(countOutputPaths("you",devices))

# PART 2
cache = {}
def countPaths(curr, end, seenFFT=False, seenDAC=False):
    
    global cache, devices

    state = (curr, seenFFT, seenDAC)
    if state in cache: return cache[state]

    if curr == "fft": seenFFT = True
    if curr == "dac": seenDAC = True

    if curr == end: return 1 if (seenFFT and seenDAC) else 0

    total = 0
    for nxt in devices[curr]:
        total += countPaths(nxt, end, seenFFT, seenDAC)

    cache[state] = total
    return total

part2 = countPaths("svr","out")
print(part2)





    
