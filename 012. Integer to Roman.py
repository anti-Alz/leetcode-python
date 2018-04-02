"""

Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num > 3999 or num < 1:
            return ""
        
        # 1000 - M; 500 - D; 100 - C; 50 - L; 10 - X; V - 5; I - 1
        ROMAN_INTEGER = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        
        result = ""
        for romanchar, intvalue in ROMAN_INTEGER:
            while num >= intvalue:
                result += romanchar
                num -= intvalue
        
        return result
