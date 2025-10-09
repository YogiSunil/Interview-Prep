# 72. Edit Distance
# Medium
# Topics
# premium lock icon
# Companies
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.


class Solution(object):
    def minDistance(self, word1, word2):
        """
        LeetCode 72 — Edit Distance

        :type word1: str
        :type word2: str
        :rtype: int

        Problem:
          Minimum operations to convert word1 -> word2 using
          insert, delete, replace (each cost 1).

        Classic DP definition (0-indexed chars; lengths m, n):
          Let dp[i][j] = min edits to convert word1[:i] -> word2[:j]
          Base:
            dp[0][j] = j   (need j inserts)
            dp[i][0] = i   (need i deletes)
          Transition:
            If word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]                     # match
            Else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # delete word1[i-1]
                    dp[i][j-1],     # insert word2[j-1]
                    dp[i-1][j-1],   # replace word1[i-1] with word2[j-1]
                )

        We’ll implement the same recurrence with a 1D rolling array
        to get O(n) extra space (n = len(word2)).
        """

        m, n = len(word1), len(word2)          # lengths of the two words

        # Edge cases (the base rows/cols cover these too, but fast-return is fine)
        if m == 0:
            return n                           # all inserts
        if n == 0:
            return m                           # all deletes

        # dp[j] will represent dp[cur_row][j] while we iterate rows.
        # Initialize the "row 0": converting "" -> word2[:j] takes j inserts.
        dp = list(range(n + 1))                # dp = [0,1,2,...,n]

        # Iterate over rows i = 1..m (for prefixes of word1)
        for i in range(1, m + 1):
            # prev_diag holds dp[i-1][j-1] (top-left diagonal) as we sweep j.
            prev_diag = dp[0]                  # dp[i-1][0]
            # New dp[0] should be i ("" <- word1[:i]): i deletes
            dp[0] = i

            # Sweep columns j = 1..n (for prefixes of word2)
            for j in range(1, n + 1):
                # Save current dp[j] (which is dp[i-1][j], the "up" cell) before overwriting
                up = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    # Characters match → carry over the diagonal
                    dp[j] = prev_diag
                else:
                    # Characters differ → 1 + min(delete, insert, replace)
                    delete_cost  = up          # dp[i-1][j]
                    insert_cost  = dp[j - 1]   # dp[i][j-1] (already updated this row)
                    replace_cost = prev_diag   # dp[i-1][j-1]
                    dp[j] = 1 + min(delete_cost, insert_cost, replace_cost)

                # Move prev_diag to the "next diagonal": dp[i-1][j] for next j+1 step
                prev_diag = up

        # dp[n] now holds dp[m][n] — the answer for full strings
        return dp[n]



#optional


class SolutionTable(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for j in range(n+1):                  # row 0 base: "" -> word2[:j]
            dp[0][j] = j
        for i in range(m+1):                  # col 0 base: word1[:i] -> ""
            dp[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # delete
                        dp[i][j-1],    # insert
                        dp[i-1][j-1],  # replace
                    )
        return dp[m][n]
