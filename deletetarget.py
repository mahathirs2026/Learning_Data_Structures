class Node:
    def __init__(self,value):
        self.value = value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self,value):
        new_node = Node(value)
        current= self.head

        if self.head == None:
            self.head = new_node

        else:
            while current.next != None:
                current = current.next
            current.next = new_node

    def printlist(self):
        current = self.head
        while current != None:  # this checks if the node exists, 
#be very careful it doesnt check if the value is a none type but wether or not the node exists to begin with
            print(current.value)
            current = current.next

    def delete(self, target):
    

        current = self.head

        if self.head.value == target:
            self.head = self.head.next
            return

        while current != None:
            
            if current.next.value == target:
                current.next = current.next.next
                return
            
            current = current.next
        
        return "target value not in list"
        
    def addafter(self, target, value):
        
        new_node = Node(value)

        current = self.head

        if self.head.value == target:
            
            new_node.next = current.next
            current. next = new_node
            return
        while current.next != None:
            if current.next.value == target:
                new_node.next = current.next.next
                current.next.next = new_node
                return
            current = current.next

        return "invalid input"



mylist = LinkedList()
olist = [1,2,3,4,5,6,2,45,89,3577,9]

for i in olist:
    mylist.append(i)

mylist.delete(5)
mylist.addafter(6,77)
mylist.printlist()

