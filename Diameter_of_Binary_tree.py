# 543. Diameter of Binary Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100



# LeetCode supplies the TreeNode class:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        LeetCode 543 — Diameter of Binary Tree

        :type root: TreeNode
        :rtype: int

        Idea:
          - The diameter is the maximum number of EDGES on any path between two nodes.
          - For each node, consider the path that goes down its left subtree and right subtree:
                diameter_through_node = left_height + right_height
          - Track the maximum of this value across all nodes.
          - A standard DFS that returns subtree height lets us compute this in one pass.

        Complexity:
          Time  : O(n)  — visit each node once
          Space : O(h)  — recursion stack (h ≤ n)
        """

        self.best = 0                         # global best diameter (in edges) found so far

        def height(node):
            """
            Returns the height (max depth in NODES) of the subtree rooted at `node`.
            While unwinding, updates self.best with the largest left_height + right_height seen.
            """
            if not node:                      # empty subtree has height 0
                return 0

            # Recursively compute left and right subtree heights
            lh = height(node.left)            # height of left subtree
            rh = height(node.right)           # height of right subtree

            # Update the best diameter: number of EDGES on path through this node
            # (edges = nodes_on_left_path + nodes_on_right_path)
            self.best = max(self.best, lh + rh)

            # Return this node's height in NODES: 1 (this node) + taller child
            return 1 + max(lh, rh)

        height(root)                          # run DFS to fill self.best
        return self.best                      # final diameter in EDGES
