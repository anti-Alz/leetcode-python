"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if (len(nums1)+len(nums2))%2 ==1:
            return self.findKth(nums1, nums2, (len(nums1)+len(nums2))//2+1)
        else:
            return (self.findKth(nums1, nums2, (len(nums1)+len(nums2))//2) + self.findKth(nums1, nums2, (len(nums1)+len(nums2))//2+1))*0.5
    

    def findKth(self, nums1, nums2, K):
        # find Kth number in two sorted arrays
        M = len(nums1)
        N = len(nums2)
        
        if M > N:
            return self.findKth(nums2, nums1, K)
        
        if not M:
            return nums2[K-1]
        
        if K==1:
            return min(nums1[0], nums2[0])
        
        if K==M+N:
            return max(nums1[M-1], nums2[N-1])
        
        p1 = min(K//2, M)
        p2 = K-p1
        
        if nums1[p1-1] <= nums2[p2-1]:
            return self.findKth(nums1[p1:], nums2, p2)
        else:
            return self.findKth(nums1, nums2[p2:], p1)
        
        
        
        