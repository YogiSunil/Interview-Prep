# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        LeetCode 54 — Spiral Matrix

        :type matrix: List[List[int]]
        :rtype: List[int]

        Idea:
          Maintain four moving boundaries:
            top, bottom, left, right
          Repeatedly traverse:
            1) left -> right across the top row, then move top down
            2) top -> bottom down the right col, then move right leftward
            3) right -> left across the bottom row (if top <= bottom), then move bottom up
            4) bottom -> top up the left col (if left <= right), then move left rightward
          Stop when the boundaries cross.

        Complexity:
          Time  : O(m * n)  (each element visited once)
          Space : O(1) extra (output list not counted)
        """

        # Guard: empty matrix
        if not matrix or not matrix[0]:
            return []

        res = []                                 # result list of elements in spiral order
        m, n = len(matrix), len(matrix[0])       # m rows, n columns

        # Initialize boundaries
        top, bottom = 0, m - 1                   # current top/bottom row indices
        left, right = 0, n - 1                   # current left/right column indices

        # Continue while boundaries are valid (not crossed)
        while top <= bottom and left <= right:

            # 1) Traverse top row from left -> right
            for c in range(left, right + 1):     # columns c = left ... right
                res.append(matrix[top][c])       # add the top row's elements
            top += 1                             # we've consumed this row; move top boundary down

            # 2) Traverse right column from top -> bottom
            for r in range(top, bottom + 1):     # rows r = top ... bottom
                res.append(matrix[r][right])     # add the rightmost column's elements
            right -= 1                           # consumed this column; move right boundary left

            # 3) Traverse bottom row from right -> left (if still within bounds)
            if top <= bottom:                    # ensure there is a remaining bottom row
                for c in range(right, left - 1, -1):  # columns c = right ... left (reverse)
                    res.append(matrix[bottom][c])
                bottom -= 1                      # move bottom boundary up

            # 4) Traverse left column from bottom -> top (if still within bounds)
            if left <= right:                    # ensure there is a remaining left column
                for r in range(bottom, top - 1, -1):  # rows r = bottom ... top (reverse)
                    res.append(matrix[r][left])
                left += 1                        # move left boundary right

        return res
