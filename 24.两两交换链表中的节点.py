#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (59.26%)
# Total Accepted:    20.4K
# Total Submissions: 34.4K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        swapLst=ListNode(0)
        tmpLst=head
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        for i in range(0,len(lst),2):
            a2Lst=tmpLst.next
            a3Lst=a2Lst.next
            # tmpa2Lst=a2Lst
            tmpLst.next=a3Lst
            a2Lst.next=tmpLst
        return tmpLst
if __name__ == "__main__":
   # 定义l1链表
   l1 = ListNode(1)
   l1.next = l11 = ListNode(2)
   l11.next = l12 = ListNode(4)
   S = Solution()
   res = S.swapPairs(l1)
   while res:
       print(res.val)
       res = res.next

