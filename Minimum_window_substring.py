# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?



from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        LeetCode 76 — Minimum Window Substring

        :type s: str
        :type t: str
        :rtype: str

        Idea (O(m + n) sliding window):
          - Count how many of each character we need from t (need map).
          - Expand the right pointer r over s, updating a "window counts" map.
          - When the current window satisfies all needed counts,
            try to shrink from the left (l) to get the minimum.
          - Track the best (smallest) window seen.

        Complexity:
          Time  : O(m + n) — each pointer l and r moves at most len(s) steps.
          Space : O(Σ)     — frequency maps over distinct characters.
        """
        # Edge case: if t is longer than s, impossible to form a window
        if len(t) > len(s):
            return ""

        # Need map: how many of each char are required
        need = Counter(t)               # e.g., t="AABC" => {'A':2, 'B':1, 'C':1}
        required = len(need)            # number of distinct chars we must satisfy

        # Window tracking
        window = Counter()              # counts of chars in current window [l..r]
        formed = 0                      # how many distinct chars currently meet required freq

        # Answer tracking: (best_len, best_l, best_r)
        best_len = float('inf')
        best_l, best_r = 0, 0

        l = 0                           # left pointer
        # Expand the window by moving r
        for r, ch in enumerate(s):      # r iterates over indices & characters in s
            window[ch] += 1             # include current char into window count

            # If this char is needed and we just met the required count for it, update formed
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try to shrink from the left while the window is valid (all required met)
            while formed == required:
                # Update best answer if this window is smaller
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l, best_r = l, r

                # Pop the leftmost char and move l forward to shrink window
                left_char = s[l]
                window[left_char] -= 1
                # If left_char was needed and we now have less than required, window becomes invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                l += 1

        # If best_len never updated, no valid window existed; else return best slice
        return "" if best_len == float('inf') else s[best_l:best_r + 1]
