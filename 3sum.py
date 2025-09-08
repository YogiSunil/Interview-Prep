# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Step 1: Sort the array
        # Sorting makes it easier to use two pointers and to skip duplicates.
        nums.sort()
        n = len(nums)

        # Result list to collect valid triplets
        res = []

        # Step 2: Loop through each number, treating nums[i] as the "anchor"
        for i in range(n):
            # If the current number is greater than 0, break the loop.
            # Why? Because after sorting, all later numbers are >= nums[i],
            # and the sum of three non-negative numbers cannot be 0.
            if nums[i] > 0:
                break

            # Skip duplicate anchors to avoid repeating triplets.
            # If nums[i] is the same as nums[i-1], we already considered it.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Two-pointer approach
            # Target we want to find is the opposite of nums[i]
            target = -nums[i]

            # Left pointer starts just after i, right pointer at the end
            l, r = i + 1, n - 1

            # While left pointer is before right pointer
            while l < r:
                # Sum of two numbers at l and r
                s = nums[l] + nums[r]

                # Case 1: Found a valid triplet
                if s == target:
                    # Add the triplet [nums[i], nums[l], nums[r]] to result
                    res.append([nums[i], nums[l], nums[r]])

                    # Move left pointer to the right
                    l += 1
                    # Skip duplicate numbers at the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Move right pointer to the left
                    r -= 1
                    # Skip duplicate numbers at the right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                # Case 2: Sum too small, need bigger numbers
                elif s < target:
                    l += 1  # move left pointer rightward (to bigger values)

                # Case 3: Sum too large, need smaller numbers
                else:
                    r -= 1  # move right pointer leftward (to smaller values)

        # Step 4: Return all collected triplets
        return res
