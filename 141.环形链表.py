#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast: # 有环才可以相等，即跳出循环，无环fast会越界
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False 

