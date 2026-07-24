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
# INORDER (Left -> Root -> Right)
#######################################################

def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.val, end=" ")

    inorder(root.right)


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


#######################################################
# Driver
#######################################################

print("Preorder :", end=" ")
preorder(root)

print("\nInorder  :", end=" ")
inorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nLevelOrder:", end=" ")
level_order(root)