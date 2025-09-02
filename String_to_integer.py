# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.



class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Remove leading whitespace from the string
        # Example: "   -42" → "-42"
        s = s.lstrip()

        # If the string becomes empty after removing spaces,
        # there is nothing to convert → return 0
        if not s:
            return 0

        # Step 2: Check if the first character is a sign
        # By default, we assume the number is positive
        sign = 1

        if s[0] == '-':
            sign = -1       # mark as negative
            s = s[1:]       # remove the sign character
        elif s[0] == '+':
            sign = 1        # explicit positive
            s = s[1:]       # remove the sign character

        # Step 3: Read digits and build the number
        # We'll stop if we see a non-digit character
        num = 0
        for char in s:
            if char.isdigit():         # check if character is 0–9
                # Multiply the existing number by 10 and add the new digit
                # Example: "42" → first '4': num=0*10+4=4 → then '2': num=4*10+2=42
                num = num * 10 + int(char)
            else:
                # If we encounter a non-digit (like 'c' in "1337c0d3"), we stop
                break

        # Step 4: Apply the sign we found earlier
        num *= sign

        # Step 5: Clamp the number into 32-bit signed integer range
        INT_MIN = -2**31        # -2147483648
        INT_MAX = 2**31 - 1     # 2147483647

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        # Step 6: Return the final integer
        return num
