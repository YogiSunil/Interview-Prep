# 91. Decode Ways
# Medium
# Topics
# premium lock icon
# Companies
# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'

# "2" -> 'B'

# ...

# "25" -> 'Y'

# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: s = "12"

# Output: 2

# Explanation:

# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:

# Input: s = "226"

# Output: 3

# Explanation:

# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:

# Input: s = "06"

# Output: 0

# Explanation:

# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution(object):
    def numDecodings(self, s):
        """
        LeetCode 91 — Decode Ways

        :type s: str
        :rtype: int

        Idea (DP with rolling variables):
          Let dp[i] = number of ways to decode s[:i] (first i characters).
          Transition for position i (1-indexed for clarity):
            - If s[i-1] != '0':  we can take the single digit → add dp[i-1]
            - If s[i-2:i] in ["10".."26"]: we can take the two-digit → add dp[i-2]

          We only need the previous two states → O(1) space:
            prev2 = dp[i-2], prev1 = dp[i-1], and curr = dp[i].

          Key zero rules:
            - '0' alone is invalid.
            - Only "10" and "20" are valid pairs involving '0'.
        """

        # Edge case: empty string (problem guarantees len>=1, but safe-guard)
        if not s:
            return 0

        # If the first char is '0', there's no valid decoding.
        if s[0] == '0':
            return 0

        # Initialize:
        # prev2 = dp[0] = 1 (empty string has 1 way)
        # prev1 = dp[1] = 1 (since s[0] != '0', first char alone is valid)
        prev2 = 1
        prev1 = 1

        # Iterate over the string starting from the second character (index 1)
        for i in range(1, len(s)):
            curr = 0  # we'll compute dp[i+1]

            # Single-digit decode valid if current char isn't '0'
            if s[i] != '0':
                curr += prev1  # add ways up to previous position

            # Two-digit decode valid if the substring s[i-1:i+1] is between "10" and "26"
            two = int(s[i-1:i+1])  # convert two-char window to int
            if 10 <= two <= 26:
                curr += prev2     # add ways up to i-1 (since we consume two chars)

            # If curr is still 0, it means neither single nor double was valid → no decoding
            if curr == 0:
                return 0

            # Slide the window:
            prev2, prev1 = prev1, curr

        # prev1 now holds dp[n] — total number of decodings for full string
        return prev1
