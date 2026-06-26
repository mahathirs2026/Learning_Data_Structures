class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def count_nodes(head):
    count = 1
    current = head
    while current.next != None:
        count+=1
        current = current.next
    return count
    
def middle_node(head):
    fast = head
    slow = head

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow.value
    

head = Node("Apple")
node2 = Node("Orange")
node3 = Node("Pineapple")
node4 = Node("Banana")
node5 = Node("Potato")


# Linking them together!
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

total_nodes = count_nodes(head)
print("Total nodes in the linked list:", total_nodes)

middle_value = middle_node(head)
print("Middle node value:", middle_value)