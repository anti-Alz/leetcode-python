"""
758. Bold Words in String

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
"""

class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        
        if not words or not S:
            return S
        
        N = len(S)
        bold = [False]*N
        result = ""
        
        for word in words:
            i = S.find(word, 0, N)
            while i>=0:
                for j in range(len(word)):
                    bold[i+j] = True
                i = S.find(word, i+1, N)
        
        for i in range(N):
            if (i==0 and bold[i]) or (i>0 and not bold[i-1] and bold[i]):
                result += "<b>"

            result += S[i]
            
            if (i==N-1 and bold[i]) or (i<N-1 and bold[i] and not bold[i+1]):
                result += "</b>"
            
        return result