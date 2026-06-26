class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        #initiate empty linked list linked list by assigning an empty node at the start
        self.head = None

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,value,):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        


    def insert_after(self,value,prev_value,):
        

        current = self.head


        while current and current.value != prev_value:
            current = current.next

        if current is None:
            print("value does not exist")
            return
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end = "->")
            current = current.next

        print("None")

    def del_val(self,delval):
        current = self.head

        if not current:
            print("empty list")
            return

        if delval == current.value:
            self.head = self.head.next
            current.value = None
            return
        
        while current.next and current.next.value != delval:
            current = current.next
        if not current.next:
            print("value does not exist")
            return
        
        current.next.value = None
        current.next = current.next.next


ll = linked_list()
ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_end(4)
ll.insert_after(5, 2)
ll.insert_after(50, 5)
ll.insert_after(35, 5)
ll.del_val(4)

ll.display()

