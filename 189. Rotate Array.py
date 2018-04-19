"""
189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?

"""

class Solution:
    def rotate(self, nums, k):
    	def reverse(nums, start, end):
    		while start < end:
	    		nums[start], nums[end] = nums[end], nums[start]
    			start +=1
    			end -=1

    	length = len(nums)
    	k = k%length
    	reverse(nums, 0, length-k-1)
    	reverse(nums, length-k, length-1)
    	reverse(nums, 0, length-1)
        

"""

"""