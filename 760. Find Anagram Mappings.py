"""
760. Find Anagram Mappings
"""

class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        if not A or not B or len(A)!=len(B):
            return []
        
        N = len(A)
        result = [0]*N
        
        for i in range(N):
            result[i] = B.index(A[i])
        
        return result
