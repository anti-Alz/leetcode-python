"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if not n:
            return False
        
        if n==1:
            return True
        
        number = n
        cycle = []
        while number!=1:
            digit_pow_sum = 0
            while number>0:
                digit_pow_sum += (number%10)**2
                number = number//10
            if digit_pow_sum==1:
                return True
            else:
                if digit_pow_sum in cycle:
                    return False
                else:
                    number = digit_pow_sum
                    cycle.append(digit_pow_sum)


"""
19
23
2334
"""