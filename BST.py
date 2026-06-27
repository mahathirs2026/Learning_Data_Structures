

class TreeNode:
    def __init__(self,value):
        # create a way for the user to input a value to go inside the treenode and set it with both left and right bieng None
        self.value = value
        self.left = None
        self.right = None

    def insert(self,new_data):
        #we need to check if new_data is bigger or smaller than the root (value).
        #we need to follow the BST rule, left is smaller than root, root is smaller than right
        if new_data < self.value:
            # is new_data is smaller than self.value then we are in the left
            if self.left is None:
                #if the left node is empty, if true we can just insert the new value here,
                #if its occupied then we need to go to the next level
                self.left = TreeNode(new_data)
            else:
                self.left.insert(new_data)

        # Repeat the process with going right, if we find that new_data is bigger than the root (value) we go right

        elif new_data > self.value:
            # we are going right
            if self.right is None:
                self.right = TreeNode(new_data)
            else:
                self.right.insert(new_data)

    def print_in_order(self):
        # the idea here is to get to the leaves of the tree until there is nothing more on the left
        #and then work our way right until there is nothing on the right
        # BST is left --> root --> right traversal
        if self.left is not None:
            self.left.print_in_order()
            # this keeps calling the function until we get to a situation when the condition is not met, i.e self.left is None
            # we are at the left most edge of the tree (smallest value) and can start printing 
        
        print(self.value, end = "-->")

        if self.right is not None:
            self.right.print_in_order()


# --- Testing our automated tree! ---
print("Building the tree...")
# Set the root to 50
root = TreeNode(50)

# Throw a bunch of random numbers at it
numbers_to_insert = [25, 75, 10, 30, 60, 80]
for num in numbers_to_insert:
    root.insert(num)

print("\nReading the tree In-Order:")
# If the logic works, this should print them in perfect numerical order!
root.print_in_order()
print("END")

        


print("hello world")