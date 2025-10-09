# 198. House Robber
# Medium
# Topics
# premium lock icon
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


class Solution(object):
    def rob(self, nums):
        """
        LeetCode 198 — House Robber

        :type nums: List[int]
        :rtype: int

        Idea (DP with two rolling states):
          - At each house i with value nums[i], you choose:
              * rob it  -> you cannot rob i-1, so value = prev2 + nums[i]
              * skip it -> keep the best up to i-1, value = prev1
          - The best up to i is max(prev1, prev2 + nums[i]).
          - We roll two variables:
              prev1 = best up to previous index (i-1)
              prev2 = best up to index (i-2)

        Complexity:
          Time  : O(n)
          Space : O(1)
        """

        # If no houses, nothing to rob.
        if not nums:
            return 0

        # Initialize rolling DP:
        # prev1 = best up to previous house (i-1)
        # prev2 = best up to the house before previous (i-2)
        prev2 = 0              # best up to index -2 (conceptually 0)
        prev1 = 0              # best up to index -1 (conceptually 0)

        # Iterate through each house's money
        for x in nums:
            # If we take this house: prev2 + x
            # If we skip this house: prev1
            take = prev2 + x
            skip = prev1

            # Current best is the max of taking vs skipping
            cur = max(take, skip)

            # Slide the window:
            # the old "prev1" becomes new "prev2",
            # and "cur" becomes new "prev1".
            prev2 = prev1
            prev1 = cur

        # prev1 holds the best total up to the last house
        return prev1
