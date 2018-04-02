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
        
        for i in range(0, N-1):
            # find a palindrome with a center s[i]
            start, end = i, i
            max_ite = min(i, N-1-i)
            ite = 0
            
            while ite<=max_ite and s[i-ite]==s[i+ite]:
                start, end = i-ite, i+ite
                ite += 1
            
            if (end-start+1) > max_palin:
                max_palin = end-start+1
                result = s[start:end+1]
            
            # find a palindrom without a center
            if s[i]==s[i+1]:
                start, end = i, i+1
                max_ite = min(i, N-2-i)
                ite = 0
                
                while ite<=max_ite and s[i-ite]==s[i+1+ite]:
                    start, end = i-ite, i+ite+1
                    ite += 1
                
                if (end-start+1) > max_palin:
                    max_palin = end-start+1
                    result = s[start:end+1]
          
        return result
