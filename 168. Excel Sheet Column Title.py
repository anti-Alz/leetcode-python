"""
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<1:
            return ""
        
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        level = 1
        length = len(chars)
        
        # to calculate how long the title is
        while (n>length) :
            n = n-length
            level +=1
            length = length * len(chars)
        
        result = ""
        n = n-1         # to adjust the index
        
        # turn a 10 hex-digit to a 26-digit
        while level > 0:
            result = chars[n%len(chars)] + result
            level -=1
            n = n//len(chars)
        
        return result

"""
1
27
523
24739
"""