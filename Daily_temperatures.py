# 739. Daily Temperatures
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        LeetCode 739 — Daily Temperatures (Monotonic Stack)

        :type temperatures: List[int]
        :rtype: List[int]

        Idea:
          - Keep a stack of indices whose temperatures are in STRICTLY DECREASING order.
          - For each day i, while today's temp is warmer than the temp at the stack's top index,
            we found the "next warmer day" for that index -> pop it and fill its waiting days.
          - Push the current index i onto the stack if no warmer day found yet.
          - Any index left in the stack by the end has answer 0 (no warmer day ahead).

        Complexity:
          Time  : O(n)  — each index is pushed and popped at most once.
          Space : O(n)  — stack + output array.
        """

        n = len(temperatures)             # number of days
        ans = [0] * n                     # default: 0 days to wait (if none found)
        stack = []                        # will store indices with decreasing temps

        # Iterate over all days by index i
        for i, today in enumerate(temperatures):
            # While there exists a previous cooler day waiting for a warmer day...
            while stack and today > temperatures[stack[-1]]:
                j = stack.pop()                  # index of that previous day
                ans[j] = i - j                   # distance from j to this warmer day i

            # Push current day index to stack; it may find its warmer day later
            stack.append(i)

        # Remaining indices in stack have no warmer day; their ans already 0
        return ans
