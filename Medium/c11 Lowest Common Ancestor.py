'''LOWEST COMMON ANCESTOR

Write a program to determine the lowest common ancestor of two nodes in a binary
search tree. You may hardcode the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29
INPUT SAMPLE:

The first argument is a path to a file that contains two values. These values
represent two nodes within the tree, one per line. E.g.:

8 52
3 29
OUTPUT SAMPLE:

Print to stdout the lowest common ancestor, one per line. Lowest means the
lowest depth in the tree, not the lowest value. E.g.:

30
8
'''

#from http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data, parent):
        """
        Node constructor
        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def insert(self, data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

tree = Node(30, None)
tree.insert(52)
tree.insert(8)
tree.insert(3)
tree.insert(20)
tree.insert(10)
tree.insert(29)
#find first common parent of the two numbers
def f(test='3 29'):#30
    left, right = test.rstrip('\n').split()
    left_parents = []
    temp = tree.lookup(int(left))[0]
    while temp != None:
        left_parents.append(temp)
        temp = temp.parent
    temp = tree.lookup(int(right))[0]
    while temp != None:
        if temp in left_parents:
            break
        temp = temp.parent
    print(temp.data)        
