def parseRange(rangeString :str):
    val1, val2 = rangeString.split("-")
    val1, val2 = list(map(int,[val1,val2]))
    return (val1,val2)

ranges, ingredients = open("input","r").read().split("\n\n")
ranges = list(map(parseRange, ranges.split("\n")))
ingredients = list(map(int,ingredients.split("\n")[:-1]))

class Range:
    def __init__(self,start,end,prev=None,next=None):
        self.start = start
        self.end = end
        self.prev = prev
        self.next = next
    def __str__(self):
        return f"<{self.start},{self.end}>"

head = Range(ranges[0][0],ranges[0][1])
for s,e in ranges:

    new = Range(s,e)

    selectL = None
    selectR = None
    curr = head
    prev = None
    while curr:

        startWithin, endWithin, wrapped = False, False, False
        if new.start >= curr.start and new.start <= curr.end: startWithin = True
        if new.end >= curr.start and new.end <= curr.end: endWithin = True
        if new.start <= curr.start and new.end >= curr.end: wrapped = True
        overlap = startWithin or endWithin or wrapped

        if overlap:
            if not selectL: selectL = curr
            selectR = curr

        if new.end < curr.start:
            break

        prev = curr
        curr = curr.next

    if selectL: # Merge
        selectL.start = min(new.start,selectL.start)
        selectL.end = max(new.end,selectR.end)
        selectL.next = selectR.next

    if not selectL:
        if curr == None: # Add tail
            prev.next = new
        if curr != None: # Add between 'prev' and 'curr'
            if prev == None: # If curr is head and new head
                head = Range(new.start,new.end,None,curr)
            else: 
                new.prev = prev
                new.next = curr
                curr.prev = new
                prev.next = new

def rewindToHead(node):
    head = None
    while node:
        head = node
        node = node.prev
    return head

head = rewindToHead(head)

# PART 01
count = 0
for i in ingredients:
    curr = head
    while curr:
        if i >= curr.start and i <= curr.end:
            count += 1
            break
        curr = curr.next
print(count)

# PART 02
count = 0
curr = head
while curr:
    count += curr.end - curr.start + 1
    curr = curr.next
print(count)