# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

class Solution(object):
    def rotate(self, matrix):
        """
        LeetCode 48 — Rotate Image (90° clockwise)

        :type matrix: List[List[int]]
        :rtype: None  (modifies matrix in place)

        Idea:
          A 90° clockwise rotation can be done in two in-place steps:
            1) Transpose the matrix (swap matrix[i][j] with matrix[j][i] for i<j)
            2) Reverse each row

          Why this works:
            - Transpose turns rows into columns.
            - Reversing each transposed row completes the clockwise rotation.

        Complexity:
          Time  : O(n^2)   (touch each element a constant number of times)
          Space : O(1)     (in-place, no extra matrix)
        """

        n = len(matrix)                              # n x n matrix size

        # -------- Step 1: Transpose in place --------
        # After this, matrix[i][j] and matrix[j][i] are swapped for i<j.
        for i in range(n):                           # iterate over each row index i
            for j in range(i + 1, n):                # only above diagonal (i<j) to avoid double swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # Example: for [[1,2,3],[4,5,6],[7,8,9]]
                # swap (0,1)<->(1,0): 2<->4, swap (0,2)<->(2,0): 3<->7, swap (1,2)<->(2,1): 6<->8
                # Transposed becomes: [[1,4,7],[2,5,8],[3,6,9]]

        # -------- Step 2: Reverse each row --------
        # Reversing each row yields the final 90° clockwise rotation.
        for i in range(n):                           # for each row i
            matrix[i].reverse()                      # reverse row in place
            # Continuing the example: reverse rows of [[1,4,7],[2,5,8],[3,6,9]]
            # -> [[7,4,1],[8,5,2],[9,6,3]] which is the desired rotation
