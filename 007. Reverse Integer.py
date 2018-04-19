"""
007. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        positive = 1;
        
        if x<0:
            return -self.reverse(-x)
        
        while x > 0:
            remainder = x %10
            x = x // 10
            reverse = reverse*10+remainder
        
        if reverse >= 0x7fffffff:
            return 0
        
        return reverse

"""
123
43234
987
"""