# 62. Unique Paths
# Medium
# Topics
# premium lock icon
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down



class Solution(object):
    def uniquePaths(self, m, n):
        """
        LeetCode 62 — Unique Paths

        :type m: int
        :type n: int
        :rtype: int

        Two ways to think about it:

        1) Combinatorics (best):
           To go from (0,0) to (m-1,n-1), you must take exactly:
             - (m-1) DOWN moves and (n-1) RIGHT moves, in any order.
           Total steps = (m-1) + (n-1) = m + n - 2.
           Choose which of these steps are DOWN (or RIGHT):
             C(m+n-2, m-1)  ==  C(m+n-2, n-1)
           We compute this combination using a multiplicative formula
           to avoid big factorials and preserve integer arithmetic.

        2) DP (classic):
           dp[i][j] = dp[i-1][j] + dp[i][j-1], with first row/col = 1.
           We can compress to one row: O(min(m,n)) space.

        We'll implement #1 (combinatorics) for optimal speed and memory.
        """

        # Make sure we always choose the smaller k in C(N, k) to minimize the loop.
        # N = total steps; k = number of DOWN moves (or RIGHT moves).
        N = m + n - 2                     # total steps to take
        k = min(m - 1, n - 1)             # choose the smaller of (m-1) and (n-1)

        # Multiplicative formula for combinations:
        #   C(N, k) = product_{i=1..k} (N - k + i) / i
        # We compute it iteratively using integer arithmetic.
        ans = 1                           # running product result (integer)
        for i in range(1, k + 1):         # i = 1..k
            ans *= (N - k + i)            # multiply numerator term
            ans //= i                     # divide by i (exact division at each step)

        return ans


#optional

class SolutionDP(object):
    def uniquePaths(self, m, n):
        """
        DP (space-optimized to O(min(m,n))).
        dp[c] represents number of ways to reach current row's column c.
        Transition: dp[c] = dp[c] (from up) + dp[c-1] (from left).
        """

        # Ensure n is the smaller dimension for less memory
        if n > m:
            m, n = n, m  # swap so that n <= m

        dp = [1] * n                  # first row: only one way (all rights)
        for _ in range(1, m):         # for each subsequent row
            for c in range(1, n):     # from column 1 to n-1
                dp[c] += dp[c - 1]    # dp[c] (up) + dp[c-1] (left)
        return dp[-1]
