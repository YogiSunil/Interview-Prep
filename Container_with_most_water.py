# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104






class Solution(object):
    def maxArea(self, height):
        """
        Two-pointer solution (O(n) time, O(1) space).
        Move the shorter side inward each step to potentially find a taller line.
        """
        # left:  start pointer at the beginning of the array
        # right: start pointer at the end of the array
        left, right = 0, len(height) - 1

        # best: keeps track of the maximum area found so far
        best = 0

        # Loop until the two pointers meet
        while left < right:
            # width: horizontal distance between the two lines
            width = right - left

            # If left line is shorter, it's the limiting height for this pair
            if height[left] < height[right]:
                # h: container height limited by the shorter line
                h = height[left]
                # area: area formed by lines at 'left' and 'right'
                area = h * width
                # Update maximum area if current area is larger
                if area > best:
                    best = area
                # Move the shorter line inward to try to find a taller one
                left += 1
            else:
                # Right line is shorter or equal; it limits the height
                h = height[right]
                area = h * width
                if area > best:
                    best = area
                # Move the shorter (or equal) line inward
                right -= 1

        # Return the maximum area found
        return best
