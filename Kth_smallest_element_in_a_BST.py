# Kth Smallest Element in a BST
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


# LeetCode provides TreeNode:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        LeetCode 230 — Kth Smallest Element in a BST

        :type root: TreeNode
        :type k: int
        :rtype: int

        Idea:
          - In a BST, an inorder traversal (Left → Node → Right) visits values in ascending order.
          - Perform iterative inorder with a stack; count nodes until we reach the k-th popped node.

        Complexity:
          Time  : O(h + k) (h = height; worst O(n) when skewed)
          Space : O(h)     (stack)
        """

        stack = []                    # manual stack for traversal
        cur = root                    # start from the root

        # Iterate as long as there are nodes to process
        while True:
            # 1) Go as left as possible, pushing nodes on the stack
            while cur:
                stack.append(cur)     # defer visiting 'cur' until after its left subtree
                cur = cur.left        # move to left child

            # 2) Pop the next node to visit (the leftmost remaining)
            cur = stack.pop()         # the next smallest node
            k -= 1                    # we've visited one more node in sorted order

            if k == 0:                # if this is the k-th node, return its value
                return cur.val

            # 3) After visiting a node, go to its right subtree
            cur = cur.right


#optional

class SolutionRecursive(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans
