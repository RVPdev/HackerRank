class Node:
    def __init__(self, info):
        # Initialize a new node with the given information and no children
        self.info = info  # Value contained in the node
        self.left = None  # Left child of the node, initialized to None
        self.right = None # Right child of the node, initialized to None
        self.level = None # Level of the node in the tree (not used in this example)

    def __str__(self):
        # String representation of the node's info value for printing
        return str(self.info) 

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty binary search tree
        self.root = None # The root of the tree, starting as None

    def create(self, val):
        # Insert a new value into the binary search tree using iterative approach
        if self.root is None:
            # If the tree is empty, create the root node with the given value
            self.root = Node(val)
        else:
            # Start at the root and find the correct place for the new value
            current = self.root
            while True:
                if val < current.info:
                    # Go left if the new value is less than the current node's value
                    if current.left:
                        # If there's a left child, move to it and continue
                        current = current.left
                    else:
                        # No left child, so create a new node and attach it here
                        current.left = Node(val)
                        break
                elif val > current.info:
                    # Go right if the new value is greater than the current node's value
                    if current.right:
                        # If there's a right child, move to it and continue
                        current = current.right
                    else:
                        # No right child, so create a new node and attach it here
                        current.right = Node(val)
                        break
                else:
                    # If the value is already in the tree, don't insert duplicates
                    break

# Node is defined as above
def preOrder(root):
    # Perform a preorder traversal of a binary tree and print each node's value
    if root is None:
        # Base case: If current node is None, return (end the recursion)
        return
    
    # Visit the root (current node) first
    print(root.info, end=' ')
    
    # Then recursively perform a preorder traversal of the left subtree
    preOrder(root.left)
    
    # Finally, recursively perform a preorder traversal of the right subtree
    preOrder(root.right)

# Example usage:
bst = BinarySearchTree()
values = [4, 2, 3, 1, 6, 5]
for value in values:
    bst.create(value)

# Perform a preorder traversal of the tree
preOrder(bst.root)  # Expected Output: 4 2 1 3 6 5 
