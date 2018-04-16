"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        curr_level, level = [root], 0
        
        while curr_level:
            level += 1
            next_level = []
            for node in curr_level:
                if not node.left and not node.right:
                    return level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
        
        return level

"""
test case
[]
[1,2,4]
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[1,null,2,null,3,4,5,null,null,null,6]
"""