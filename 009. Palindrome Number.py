"""

Determine whether an integer is a palindrome. Do this without extra space.

"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x <0:
            return False
        
        if x < 10:
            return True
        
        n=1

        while x // pow(10, n) >=10:
            n += 1
        
        while x // pow(10, n) == x%10 and n > 0:
            x = (x - (x // pow(10,n)) * pow(10,n) - (x % 10))//10
            n -= 2
            if x==0 or (x < 10 and n < 1):
                return True
        
        return False

    

    # Another solution but need extra space
    """
    def isPalindrome(self, x):
        str_x = str(x)
        return str_x == str_x[::-1]
    """
