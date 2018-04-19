"""
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        # delete val at head
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None
        
        ite = head
        prev = head
        
        while ite:
            # if found val, delete it
            if(ite.val == val):
                prev.next = ite.next
                ite = ite.next
            # otherwise next
            else:   
                prev = ite
                ite = ite.next

        return head

"""
[1,2,6,3,4,5,6]
6
"""