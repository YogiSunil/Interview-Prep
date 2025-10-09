# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.



# LeetCode provides TreeNode:
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        LeetCode 235 — Lowest Common Ancestor of a Binary Search Tree

        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Idea (use BST ordering):
          - In a BST, for any node 'x':
              all nodes in 'x.left' have values < x.val
              all nodes in 'x.right' have values > x.val
          - Walk down from the root:
              * If both p and q are < current.val, LCA lies in the LEFT subtree.
              * If both p and q are > current.val, LCA lies in the RIGHT subtree.
              * Otherwise (they split or one equals current), current is the LCA.

        Complexity:
          Time  : O(h)     (h = tree height; worst O(n), avg O(log n) in balanced BST)
          Space : O(1)     (iterative; no recursion stack)
        """

        # Normalize small/big to make comparisons slightly clearer (optional)
        small = min(p.val, q.val)    # smaller of the two values
        big   = max(p.val, q.val)    # larger of the two values

        cur = root                   # start from the root
        while cur:                   # walk down until we find the split point
            if big < cur.val:        # both targets are strictly less than cur => go LEFT
                cur = cur.left
            elif small > cur.val:    # both targets are strictly greater than cur => go RIGHT
                cur = cur.right
            else:
                # We are at the split point:
                # small <= cur.val <= big  → cur is between p and q (or equals one)
                # This is the LCA by BST property.
                return cur

        # Problem guarantees p and q exist in the BST; this line shouldn't be reached.
        return None
