'''
这个题目是直接抄答案的！！把答案慢慢拿笔写一遍思路！！！顺序要对！
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev