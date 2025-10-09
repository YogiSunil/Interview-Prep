# 102. Binary Tree Level Order Traversal
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# LeetCode provides TreeNode:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        LeetCode 102 — Binary Tree Level Order Traversal

        :type root: TreeNode
        :rtype: List[List[int]]

        Idea (BFS by levels):
          - Use a queue to traverse the tree level by level (left to right).
          - For each level, pop exactly 'level_size' nodes from the queue,
            record their values, and push their children for the next level.

        Complexity:
          Time  : O(n)  — visit each node once.
          Space : O(n)  — queue can hold a level's nodes; output stores all values.
        """

        # If the tree is empty, return empty list
        if not root:
            return []

        res = []                     # final list of levels, e.g., [[3],[9,20],[15,7]]
        q = deque([root])            # queue initialized with the root node

        # While there are nodes to process
        while q:
            level_vals = []          # values for the current level
            level_size = len(q)      # number of nodes in this level (fixed before processing)

            # Process exactly 'level_size' nodes (the current level)
            for _ in range(level_size):
                node = q.popleft()   # pop the next node from the left of the queue
                level_vals.append(node.val)  # record its value

                # Push the children into the queue for the next level (if they exist)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # After consuming the current level, append its values to the result
            res.append(level_vals)

        return res




#optional 

class SolutionDFS(object):
    def levelOrder(self, root):
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):      # first time reaching this depth → new list
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res
