# 424. Longest Repeating Character Replacement
# Medium
# Topics
# premium lock icon
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length




from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        LeetCode 424 — Longest Repeating Character Replacement

        :type s: str
        :type k: int
        :rtype: int

        Idea (O(n) sliding window):
          - Maintain a window [l..r] and counts of letters inside it.
          - Let max_freq be the count of the most frequent letter in the window.
          - A window is valid if (window_size - max_freq) <= k,
            because we can change at most k other letters to the majority letter.
          - Expand r each step; if the window becomes invalid, move l forward
            until it becomes valid again. Track the largest valid window size.

        Complexity:
          Time  : O(n) — each index enters and leaves the window at most once.
          Space : O(1) — counts for uppercase letters (≤ 26).
        """

        # Frequency map for current window; defaultdict avoids key checks
        count = defaultdict(int)

        l = 0                 # left boundary of window
        max_freq = 0          # highest frequency of a single char in current window
        best = 0              # best (max) valid window length found

        # Iterate r over the string once (right boundary of window)
        for r, ch in enumerate(s):
            count[ch] += 1                    # include current char in the window
            max_freq = max(max_freq, count[ch])  # update the max single-char frequency

            # Current window size = (r - l + 1).
            # Needed replacements to make all chars equal = window_size - max_freq.
            # If we need more than k replacements, shrink from the left.
            while (r - l + 1) - max_freq > k:
                left_char = s[l]              # char about to leave window
                count[left_char] -= 1         # decrement its count
                l += 1                        # shrink window from the left

                # Note: we don't recompute max_freq downward here.
                # It's safe because a larger max_freq only makes the condition easier
                # to satisfy. At worst, window shrinks until condition holds again.

            # Update best with current valid window length
            best = max(best, r - l + 1)

        return best
