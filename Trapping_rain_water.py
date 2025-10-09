# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

class Solution(object):
    def trap(self, height):
        """
        LeetCode 42 — Trapping Rain Water (Two-Pointers)

        :type height: List[int]
        :rtype: int

        Intuition:
          - Water above index i is limited by the shorter of the tallest bars to its LEFT and RIGHT.
          - If we move two pointers from both ends, we can maintain:
              left_max  = max height seen so far from the left
              right_max = max height seen so far from the right
          - At each step, we move the pointer at the side with the SMALLER max,
            because that side is the limiting wall. The trapped water there is
            (that_side_max - height[ptr]) if positive.

        Complexity:
          Time  : O(n) — each index visited at most once.
          Space : O(1) — only a few variables.
        """

        n = len(height)            # number of bars
        if n <= 2:                 # with fewer than 3 bars, no water can be trapped
            return 0

        left, right = 0, n - 1     # two pointers starting at both ends
        left_max = 0               # highest bar encountered from the left so far
        right_max = 0              # highest bar encountered from the right so far
        water = 0                  # accumulator for total trapped water

        # Process while pointers haven't crossed
        while left <= right:
            # Update running maxima for both sides
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # Decide which side limits water this round
            if left_max <= right_max:
                # Left side is the bottleneck: water at 'left' is limited by left_max
                water += left_max - height[left]   # if height[left] < left_max, this adds positive water; else adds 0
                left += 1                          # move left pointer inward
            else:
                # Right side is the bottleneck: water at 'right' is limited by right_max
                water += right_max - height[right] # similar logic for the right side
                right -= 1                         # move right pointer inward

        return water
