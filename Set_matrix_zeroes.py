# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?




class Solution(object):
    def setZeroes(self, matrix):
        """
        LeetCode 73 — Set Matrix Zeroes (Constant-Space Solution)

        :type matrix: List[List[int]]
        :rtype: None (modifies matrix in place)

        Idea (why O(1) extra space works):
          - Use the matrix itself to remember which rows/cols must be zero.
          - Specifically, use the first row and the first column as "marker" storage.
          - We also separately remember if the *first row* or *first column* themselves
            need to be zeroed (two booleans), so we don't lose that info.

        Steps:
          1) Scan first row & first column to set two flags: first_row_zero, first_col_zero.
          2) For every cell (i, j) with i>0 and j>0:
                if matrix[i][j] == 0:
                    mark its row and column by setting matrix[i][0] = 0 and matrix[0][j] = 0
          3) Do a second pass (i>0, j>0) and zero cells where row/col is marked.
          4) Finally, zero the first row if first_row_zero, and zero the first column if first_col_zero.

        Complexity:
          Time  : O(m * n) — two full scans of the matrix
          Space : O(1)     — only a couple of booleans; markers are stored in-place
        """

        # m = number of rows, n = number of columns
        m = len(matrix)                      # count rows
        n = len(matrix[0])                   # count cols (matrix is guaranteed non-empty)

        # Determine whether the FIRST ROW should be zeroed.
        first_row_zero = False               # flag for entire first row
        for j in range(n):                   # scan all columns of row 0
            if matrix[0][j] == 0:           # if any element is zero
                first_row_zero = True        # remember to zero-out row 0 later
                break                        # no need to keep scanning

        # Determine whether the FIRST COLUMN should be zeroed.
        first_col_zero = False               # flag for entire first column
        for i in range(m):                   # scan all rows of column 0
            if matrix[i][0] == 0:           # if any element is zero
                first_col_zero = True        # remember to zero-out col 0 later
                break                        # no need to keep scanning

        # Use first row and first column as markers for the rest of the grid.
        for i in range(1, m):                # start from row 1 (leave row 0 for markers)
            for j in range(1, n):            # start from col 1 (leave col 0 for markers)
                if matrix[i][j] == 0:        # if the current cell is zero
                    matrix[i][0] = 0         # mark this row: set the first cell of the row to 0
                    matrix[0][j] = 0         # mark this column: set the first cell of the column to 0

        # Zero cells based on markers in the first row/column.
        for i in range(1, m):                # again skip first row
            for j in range(1, n):            # again skip first column
                # If either its row or column is marked (i.e., first cell is zero),
                # then this cell must become zero.
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # If the first row originally needed to be zeroed, zero it now.
        if first_row_zero:                   # check the saved flag
            for j in range(n):               # set all entries in row 0 to zero
                matrix[0][j] = 0

        # If the first column originally needed to be zeroed, zero it now.
        if first_col_zero:                   # check the saved flag
            for i in range(m):               # set all entries in column 0 to zero
                matrix[i][0] = 0             # (do this after inner area is processed)
