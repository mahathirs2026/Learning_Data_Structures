class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedlist():
    def __init__(self,):
        self.head = None

    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node


old_list = [1,2,3,4,5,"apple","oranges","potatoes","mangoes","grapes"]
mylist = linkedlist()

for i in old_list:
    mylist.append(i)

current = mylist.head
while current != None:
    print(current.value)
    current = current.next