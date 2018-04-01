"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ""
        
        max_palin = 1
        result = s[0]
        
        N = len(s)
        
        for i in range(N):
            # find the next character same as s[i]
            j = s.rfind(s[i], i+1, N)
            
            # if found, start check
            while j>=0 and j-i+1 > max_palin:  
                if self.isPalindrome(s[i:j+1]) and j-i+1 >max_palin:
                    max_palin = j-i+1
                    result = s[i:j+1]
                    break
                
                # find next s[i]
                j = s.rfind(s[i], i+1, j)
                
        return result
        
    def isPalindrome(self, string):
        if not string:
            return True
        
        if len(string)==1:
            return True
        
        start, end = 0, len(string)-1
        
        while start<end:
            if string[start]!=string[end]:
                return False
            start += 1
            end -= 1
        
        return True
        
        