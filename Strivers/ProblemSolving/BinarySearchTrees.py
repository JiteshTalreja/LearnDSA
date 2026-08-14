"""
============================================================
                    BINARY TREE CHEAT SHEET
============================================================

Definition
----------

A Binary Tree is a tree where each node has at most
two children:

Left Child
Right Child

Unlike BST, there is NO ordering.

------------------------------------------------------------

Example

            1
          /   \
         2     3
        / \   / \
       4  5  6   7

------------------------------------------------------------

Terminology

Root
    Top-most node.

Parent
    Node having children.

Child
    Node connected below parent.

Leaf
    Node with no children.

Sibling
    Nodes with same parent.

Ancestor
    Parent, Grandparent, ...

Descendant
    Child, Grandchild, ...

Subtree
    Tree rooted at any node.

Height
    Number of edges in longest path from
    node to leaf.

Depth
    Number of edges from root to node.

Level
    Root is level 0.

------------------------------------------------------------

Binary Tree vs BST

Binary Tree

No ordering.

        10
       /  \
      50   2

Perfectly valid.

BST

Left < Root < Right

        10
       /  \
      5    20

------------------------------------------------------------

Representation

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

------------------------------------------------------------

Recursive Structure

Every tree consists of

Root

Left Subtree

Right Subtree

This is why recursion fits naturally.

------------------------------------------------------------

Tree Traversals

There are 4 major traversals.

1. Preorder

Root

Left

Right

(Root first)

------------------------------------------------------------

2. Inorder

Left

Root

Right

(Root in middle)

For BST

Inorder is ALWAYS sorted.

------------------------------------------------------------

3. Postorder

Left

Right

Root

(Root last)

------------------------------------------------------------

4. Level Order

Level by Level

Uses Queue (BFS)

------------------------------------------------------------

Traversal Memory Trick

Preorder

Root Left Right

RLR


Inorder

Left Root Right

LRR


Postorder

Left Right Root

LRR (Root Last)

Easy Trick

Preorder

Root comes FIRST

Inorder

Root comes IN between

Postorder

Root comes LAST

------------------------------------------------------------

Example

            1
          /   \
         2     3
        / \   / \
       4  5  6  7


Preorder

1 2 4 5 3 6 7


Inorder

4 2 5 1 6 3 7


Postorder

4 5 2 6 7 3 1


Level Order

1 2 3 4 5 6 7

------------------------------------------------------------

Traversal Templates

Preorder

visit(node)

dfs(left)

dfs(right)


Inorder

dfs(left)

visit(node)

dfs(right)


Postorder

dfs(left)

dfs(right)

visit(node)

------------------------------------------------------------

Base Case

if node is None:
    return

------------------------------------------------------------

DFS vs BFS

DFS

Recursion / Stack

Preorder

Inorder

Postorder


BFS

Queue

Level Order

------------------------------------------------------------

Complexities

Traversal

Time

O(n)

Every node visited once.


Space

O(h)

Recursion stack.

Worst

O(n)

Balanced

O(log n)

------------------------------------------------------------

Important Interview Problems

✓ Preorder
✓ Inorder
✓ Postorder
✓ Level Order
✓ Height
✓ Diameter
✓ Balanced Tree
✓ Same Tree
✓ Symmetric Tree
✓ Maximum Depth
✓ Lowest Common Ancestor
✓ Path Sum
✓ Right Side View
✓ Vertical Traversal

------------------------------------------------------------

Golden Rule

Trees are recursive.

For every problem ask:

"What should I do with

Current Node

Left Subtree

Right Subtree?"

If you can answer that,

the recursion writes itself.

============================================================
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#######################################################
# PREORDER (Root -> Left -> Right)
#######################################################

def preorder(root):
    if root is None:
        return

    print(root.val, end=" ")

    preorder(root.left)
    preorder(root.right)

#######################################################
# ITERATIVE PREORDER (Root -> Left -> Right)
#######################################################

def iterative_preorder(root):
    if root is None:
        return 
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        

#######################################################
# INORDER (Left -> Root -> Right)
#######################################################

def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.val, end=" ")

    inorder(root.right)

#######################################################
# ITERATIVE INORDER (Left -> Root -> Right)
#######################################################

def iterative_indorder(root):
    if root is None:
        return 

    stack = []
    current = root

    while stack or current:

        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=" ")
        current =current.right

#######################################################
# POSTORDER (Left -> Right -> Root)
#######################################################

def postorder(root):
    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.val, end=" ")

#######################################################
# ITERATIVE POSTORDER (Left -> Right -> Root) using 2 Stacks
#######################################################

def iterative_postorder(root):
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().val, end=" ")

#######################################################
# ITERATIVE POSTORDER (Left -> Right -> Root) using 1 Stacks
#######################################################

def iterative_postorder_1(root):
    stack =[]
    curr = root
    last_visited = None

    while stack or curr:

        while curr:
            stack.append(curr)
            curr = curr.left

        peek = stack[-1]

        if peek.right and last_visited != peek.right:
            curr = peek.right
        else:
            print(peek.val, end=' ')
            last_visited = stack.pop()

#######################################################
# ALL TRAVERSALS
#######################################################

def all_traversals(root):
    if root is None:
        return [], [], []

    preorder = []
    inorder = []
    postorder = []

    stack =[(root, 1)]

    while stack:
        node, state = stack.pop()

        if state == 1:
            preorder.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))
        elif state ==2:
            inorder.append(node.val)

            stack.append((node, 3))

            if node.right:
                stack.append((node.right, 1))
        else:
            postorder.append(node.val)
    return preorder, inorder, postorder

#######################################################
# LEVEL ORDER (BFS)
#######################################################

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

#######################################################
# Maximum Depth in Binary Tree
#######################################################

def max_depth(root):

    if root is None:
        return 0

    lmax = max_depth(root.left)
    rmax = max_depth(root.right)

    return 1+max(lmax, rmax)

#######################################################
# L15. Check for Balanced Binary Tree
#######################################################

def is_balanced(root):

    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1+max(left, right)
    return dfs(root) != -1

#######################################################
# L16. Diameter of Binary Tree
#######################################################

def diameter(root):

    diameter = 0

    def dfs(node):
        nonlocal diameter
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left+right)

        return max(left, right)+1
    dfs(root)
    return diameter

#######################################################
# L17. Maximum Path Sum in Binary Tree 
#######################################################

def max_path(root):

    max_path = float("-inf")

    def dfs(node):
        nonlocal max_path
        if node is None:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        max_path = max(max_path, left + right + node.val)

        return max(left, right)+node.val
    dfs(root)
    return max_path

#######################################################
# L18. Check it two trees are Identical or Not  
#######################################################

def is_identical(root1, root2):

    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False
    return (is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)) 

#######################################################
# L19. Zig-Zag or Spiral Traversal in Binary Tree  
#######################################################

def zigzag_traversal(root):

    queue = deque([root])
    res = []
    left_to_right = True
    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()
        res.append(level)
        left_to_right = not left_to_right
    return res

#######################################################
# L20. Boundary Traversal in Binary Tree  
#######################################################

def boundary_traversal(root):

    if root is None:
        return []

    def is_leaf(node):
        return node.left is None and node.right is None

    if is_leaf(root):
        return [root.val]
    
    ans = [root.val]

    def left_boundary(node):
        while node:
            if not is_leaf(node):
                ans.append(node.val)
            if node.left:
                node = node.left
            else:
                node=node.right

    def right_boundary(node):
        temp = []

        while node:

            if not is_leaf(node):
                temp.append(node.val)
            if node.right:
                node = node.right
            else:
                node=node.left
        ans.extend(temp[::-1])
    def add_leaf(node):
        if node is None:
            return

        if is_leaf(node):
            ans.append(node.val)
            return

        add_leaf(node.left)
        add_leaf(node.right)

    left_boundary(root.left)

    add_leaf(root)

    right_boundary(root.right)
    return ans

#######################################################
# L21. Vertical Order Traversal of Binary Tree   
#######################################################

def vertical_traversal(root):
    if root is None:
        return []

    queue = deque([(root, 0, 0)])
    columns = {}

    while queue:
        node, row, col = queue.popleft()

        if col not in columns:
            columns[col] = []

        columns[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row+1, col-1))
        if node.right:
            queue.append((node.right, row+1, col+1))

    ans = []
    for cols in sorted(columns):
        nodes = columns[cols]

        nodes.sort()

        level = []

        for row, val in nodes:
            level.append(val)

        ans.append(level)
    return ans

#######################################################
# L22. Top View of Binary Tree  
#######################################################

def top_view(root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    levels = {}

    while queue:
        node, col = queue.popleft()

        if col not in levels:
            levels[col] = (col, node.val)

        if node.left:
            queue.append((node.left, col-1))
        if node.right:
            queue.append((node.right, col+1))

    ans = []
    for cols in sorted(levels):
        ans.append(levels[cols])

    return ans

#######################################################
# L23. Bottom View of Binary Tree  
#######################################################

def bottom_view(root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    levels = {}

    while queue:
        node, col = queue.popleft()

        levels[col] = (col, node.val)

        if node.left:
            queue.append((node.left, col-1))
        if node.right:
            queue.append((node.right, col+1))

    ans = []
    for cols in sorted(levels):
        ans.append(levels[cols])

    return ans

#######################################################
# L24. Right/Left View of Binary Tree
#######################################################

def right_view(root):
    ans = []

    def traverse(node, level):
        if node is None:
            return

        if level == len(ans):
            ans.append(node.val)

        traverse(node.right, level+1)
        traverse(node.left, level+1)
    traverse(root, 0)
    return ans

def left_view(root):
    ans = []

    def traverse(node, level):
        if node is None:
            return

        if level == len(ans):
            ans.append(node.val)

        traverse(node.left, level+1)
        traverse(node.right, level+1)
    traverse(root, 0)
    return ans


#######################################################
# Example Tree
#######################################################

#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root2 = TreeNode(1)

root2.left = TreeNode(2)
root2.right = TreeNode(3)

root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

root2.right.left = TreeNode(6)
root2.right.right = TreeNode(8)


#######################################################
# Driver
#######################################################

print("Preorder :", end=" ")
preorder(root)

print("\nIterative Preorder :", end=" ")
iterative_preorder(root)

print("\nInorder  :", end=" ")
inorder(root)

print("\nIterative Inorder :", end=" ")
iterative_indorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nIterative Postorder:", end=" ")
iterative_postorder(root)

print("\nIterative Postorder 1 stack:", end=" ")
iterative_postorder_1(root)

print("\nLevelOrder:", end=" ")
level_order(root)

print("\n All Traversals :", end=" ")
print(all_traversals(root))

print("\n max depth :", end=" ")
print(max_depth(root))

print("\n diameter :", end="")
print(diameter(root))

print("\n max_path :", end="")
print(max_path(root))

print("\n is_identical :", end="")
print(is_identical(root, root2))

print("\n zigzag traversal :", end="")
print(zigzag_traversal(root))

print("\n boundary traversal :", end="")
print(boundary_traversal(root))

print("\n vertical traversal :", end="")
print(vertical_traversal(root))

print("\n top view :", end="")
print(top_view(root))

print("\n bottom view :", end="")
print(bottom_view(root))

print("\n right view :", end="")
print(right_view(root))

print("\n left view :", end="")
print(left_view(root))