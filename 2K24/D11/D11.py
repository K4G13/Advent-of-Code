initial_state = list(map(int,open("input").read().split()))

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return str(elements)
    
    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def blink(self):
        current = self.head
        while current:

            if current.value == 0: 
                current.value = 1
                current = current.next
                continue

            if len(str(current.value)) % 2 == 0:

                str_val = str(current.value)
                val_a, val_b = int(str_val[:len(str_val)//2]), int(str_val[len(str_val)//2:])
                
                current.value = val_a
                new_node = Node(val_b)
                new_node.next = current.next
                current.next = new_node
                self.size += 1

                current = current.next.next
                continue

            else:
                current.value *= 2024
                current = current.next
                continue            
        
stones = LinkedList()
for el in initial_state: stones.add(el)

BLINKS = 25
for _ in range(BLINKS): stones.blink()
print(len(stones))