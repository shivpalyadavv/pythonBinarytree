class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val  = key

# create root
root = Node(1)
#''' tree for above statement
#        1
#      /  \
#   None  None'''

root.left = Node(2);
root.right = Node(3);

#'''2 and 3 become left and right children of 1
#               1
#             /  \'''
#            2    3
#         /   \  /  \

root.left.left = Node(4)
#'''4 become left childe of 2
#           1
#         /  \
#        2    3
#      /  \  /  \
#     4   N N   N
#   /  \
#  N    N ''''
