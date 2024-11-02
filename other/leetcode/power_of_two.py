# 231. Power of Two
# Link in Leetcode https://leetcode.com/problems/power-of-two/description/
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:
# Input: n = 3
# Output: false

def is_power_of_two(n: int) -> bool:
    # if n <= 0:
    #     return False
    # if n == 1:
    #     return True
    # while n % 2 == 0:
    #     n = n // 2
    #     return False
    # return True
    power = 1
    while 2 ** power < n:
        power += 1

    return 2 ** power == n


print(is_power_of_two(1))
print(is_power_of_two(16))
print(is_power_of_two(3))

#  Link in solution -> https://ithelp.ithome.com.tw/articles/10267400 Needs explanation
def isPowerOfTwo(n: int) -> bool:
    if n < 1:
        return False
    n = bin(n)
    count = 0
    for i in n[2:]:
        if i == "1":
            count += 1
    return count == 1

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
