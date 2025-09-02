# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?
 


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers are never palindromes because of the '-'
        if x < 0:
            return False

        # Convert to string
        s = str(x)

        # Check if string equals its reverse
        return s == s[::-1]



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers and numbers ending with 0 (except 0 itself)
        # cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Build the reversed number only for the second half
        while x > reversed_half:
            digit = x % 10                   # take last digit
            reversed_half = reversed_half * 10 + digit
            x //= 10                         # remove last digit from x

        # Case 1: even number of digits → x should equal reversed_half
        # Case 2: odd number of digits → ignore the middle digit by reversed_half//10
        return x == reversed_half or x == reversed_half // 10
