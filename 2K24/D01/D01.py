f = open("input")
raw_data = f.read()
f.close()

LList = []
RList = []

for row in raw_data.split('\n'):
    x,y = row.split()
    LList.append(x)
    RList.append(y)

LList.sort()
RList.sort()

difference = []
for i in range(len(LList)):
    difference.append( abs( int(LList[i]) - int(RList[i]) ) )

print(sum(difference))

#PART 2

similarity_score = 0
for el in LList:
    count = RList.count(el)
    similarity_score += int(el)*count

print(similarity_score)