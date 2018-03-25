"""
Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        list.sort(nums)
        
        max_length, length = 0, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                length +=1
                max_length = max(max_length, length)
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = 1
         
        max_length = max(max_length, length)

        return max_length

if __name__ == "__main__":
    print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print Solution().longestConsecutive([])
    print Solution().longestConsecutive([1, 2, 3, 4, 5])
    print Solution().longestConsecutive([0, 1, 1, 2, 5, 3, 5, 7, 10, 4])
    print Solution().longestConsecutive([200, -1, 3])
