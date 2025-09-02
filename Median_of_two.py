# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the shorter array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Number of elements in left partition
        left, right = 0, m
        while left <= right:
            # Partition nums1 at position i
            i = (left + right) // 2
            # Partition nums2 at position j to make left partition size = half
            j = half - i
            # Get boundary values
            # Left partition maximums
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            # Right partition minimums
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_right_min = float('inf') if j == n else nums2[j]
            # Check if we found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Perfect partition found!
                if total % 2 == 1:
                    # Odd total length - median is max of left partition
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    # Even total length - median is average of max(left) and min(right)
                    left_max = max(nums1_left_max, nums2_left_max)
                    right_min = min(nums1_right_min, nums2_right_min)
                    return (left_max + right_min) / 2.0
            elif nums1_left_max > nums2_right_min:
                # nums1 partition is too far right, move left
                right = i - 1
            else:
                # nums1 partition is too far left, move right
                left = i + 1
        # Should never reach here with valid input
        return 0.0

if __name__ == "__main__":
    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print("Median of [1,3] and [2]:", result)

    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print("Median of [1,2] and [3,4]:", result)


    if __name__ == "__main__":
        # Example 1
        nums1 = [1, 3]
        nums2 = [2]
        sol = Solution()
        result = sol.findMedianSortedArrays(nums1, nums2)
        print("Median of [1,3] and [2]:", result)

        # Example 2
        nums1 = [1, 2]
        nums2 = [3, 4]
        result = sol.findMedianSortedArrays(nums1, nums2)
        print("Median of [1,2] and [3,4]:", result)
