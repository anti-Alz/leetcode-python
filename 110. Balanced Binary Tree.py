"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        self.balance = True
        self.getDepth(root)
        
        return self.balance
        

    # recursive function, get depth of a tree        
    def getDepth(self, root):
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        
        if abs(left_depth - right_depth) > 1:
            self.balance = False
        
        return 1+max(left_depth, right_depth)
    