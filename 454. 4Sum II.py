"""

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 2^31 - 1.


"""



class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        if not (len(A)==len(B) and len(A)==len(C) and len(A)==len(D)):
            return 0
        
        count = 0
        sums = collections.defaultdict(int)
        
        for a in A:
            for b in B:
                sums[a+b] += 1
        
        for c in C:
            for d in D:
                count += sums[-c-d]
                
        return count