# Link in task  https://leetcode.com/problems/palindrome-number/description/
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def ispalindrome(x: int) -> bool:
    x_text = str(x)
    if x_text == x_text[::-1]:
        return True
    else:
        return False



print(ispalindrome(-121))