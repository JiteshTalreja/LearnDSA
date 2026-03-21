
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __r_contains(self, current_node, value):

        if current_node == None:
            return False
        ## BASE condition
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):

        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)


    def min_value(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node


    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    ## BREADTH FIRST SEARCH ( BFS )

    def bfs(self):

        current_node = self.root
        queue = []
        result = []

        queue.append(current_node)

        while len(queue) >0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result


    ## DEPTH FIRST SEARCH ( DFS ) - PRE ORDER
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    ## DEPTH FIRST SEARCH ( DFS ) - POST ORDER
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

        ## DEPTH FIRST SEARCH ( DFS ) - In ORDER
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    """
    BST: Validate BST ( ** Interview Question)
    You are tasked with writing a method called is_valid_bst in the BinarySearchTree class that checks whether a binary search tree is a valid binary search tree.

    Your method should use the dfs_in_order method to get the node values of the binary search tree in ascending order, and then check whether each node value is greater than the previous node value.

    If the node values are not sorted in ascending order, the method should return False, indicating that the binary search tree is not valid.

    If all node values are sorted in ascending order, the method should return True, indicating that the binary search tree is a valid binary search tree.
    """
    def is_valid_bst(self):

        in_order_bst = self.dfs_in_order()

        i = 0
        for j in range(1, len(in_order_bst)):
            if in_order_bst[i] >= in_order_bst[j]:
                return False
            i += 1
        return True

    """
    BST: Kth Smallest Node ( ** Interview Question)
    Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.
    
    The solution to this problem usually involves traversing the tree in-order (left, root, right) and keeping track of the number of nodes visited until you find the kth smallest element. There are two main approaches to doing this:
    
    Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need to be visited, starting with the leftmost node. At each step, you pop a node off the stack, decrement the kth smallest counter, and check whether you have found the kth smallest element. If you have not, you continue traversing the tree by moving to the right child of the current node.
    
    Recursive approach: This approach involves recursively traversing the tree in-order and keeping track of the number of nodes visited until you find the kth smallest element. You can use a helper function that takes a node and a value of k as input, and recursively calls itself on the left and right children of the node until it finds the kth smallest element.
    
    Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.
    """

    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []
        # start at the root of the tree
        temp = self.root

        while stack or temp:
            # traverse to the leftmost node
            while temp:
                # add the node to the stack
                stack.append(temp)
                temp = temp.left

            # pop the last node added to the stack
            temp = stack.pop()
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:
                return temp.value

            # move to the right child of the node
            temp = temp.right

            # if k is greater than the number of nodes in the tree, return None
        return None

    def r_kth_smallest(self, k):
        # initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        # call the helper function with the root node and k
        return self.kth_smallest_helper(self.root, k)

    def kth_smallest_helper(self, node, k):
        if node is None:
            # if the current node is None, return None
            return None

        # recursively call the helper function on the left child of the node and store the result in left_result
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            # if left_result is not None, return it
            return left_result

        # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            # if the kth smallest element is found, return the value of the current node
            return node.value

        # recursively call the helper function on the right child of the node and store the result in right_result
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            # if right_result is not None, return it
            return right_result

        # if the kth smallest element is not found, return None
        return None

    """
    Invert a Binary tree
    """

    def __invert_tree(self, node):
        if node is None:
            return None

        temp = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)

        return node

tree = BinarySearchTree()
tree.r_insert(47)
tree.r_insert(21)
tree.r_insert(76)
tree.r_insert(18)
tree.r_insert(27)
tree.r_insert(52)
tree.r_insert(82)

print(tree.dfs_pre_order())
print(tree.dfs_post_order())
print(tree.dfs_in_order())