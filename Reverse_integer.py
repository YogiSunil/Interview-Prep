# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
# signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1  # Maximum 32-bit signed integer (2,147,483,647)
        INT_MIN = -2**31     # Minimum 32-bit signed integer (-2,147,483,648)

        # Determine the sign of x (positive or negative)
        sign = 1 if x >= 0 else -1  # 1 for positive, -1 for negative
        x = abs(x)                  # Work with the absolute value for reversal
        result = 0                  # This will store the reversed number

        while x != 0:
            digit = x % 10          # Extract the last digit of x
            x //= 10                # Remove the last digit from x

            # Check for overflow BEFORE updating result
            if sign == 1:  # If original number was positive
                # If result * 10 + digit would exceed INT_MAX, return 0
                if result > (INT_MAX - digit) // 10:
                    return 0
                # Edge case: if result is exactly at the threshold, check the digit
                if result == (INT_MAX - digit) // 10 and digit > INT_MAX % 10:
                    return 0
            else:  # If original number was negative
                # If -(result * 10 + digit) would be less than INT_MIN, return 0
                if result > (-INT_MIN - digit) // 10:
                    return 0
                # Edge case for negative threshold
                if result == (-INT_MIN - digit) // 10 and digit > (-INT_MIN) % 10:
                    return 0

            result = result * 10 + digit  # Add the digit to the reversed number

        # Restore the original sign to the result
        return sign * result
    
# ----------------------------
# TEST CASES with Expected Output
# ----------------------------

s = Solution()

print(s.reverse(123))         # Expected 321
print(s.reverse(-123))        # Expected -321
print(s.reverse(120))         # Expected 21
print(s.reverse(0))           # Expected 0
print(s.reverse(1534236469))  # Expected 0 (overflow)
print(s.reverse(-2147483412)) # Expected -2143847412 (still valid)
print(s.reverse(2147483647))  # Expected 0 (overflow when reversed)
print(s.reverse(-2147483648)) # Expected 0 (overflow when reversed)