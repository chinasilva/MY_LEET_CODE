#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (45.41%)
# Total Accepted:    25.4K
# Total Submissions: 56K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # lst=[]
        # tmpLst=head
        # while head:
        #    lst.append(head.val)
        #    head=head.next
        # lst= set(lst) 
        # lst= list(lst)
        # # tmpLst=ListNode(0)
        # tmp2Lst=tmpLst
        # for i in range(len(lst)):
        #     if tmpLst.val!= lst[i]:
        #         tmpLst=tmpLst.next
        # return tmpLst
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
if __name__ == "__main__":
   # 定义l1链表
   l1 = ListNode(1)
   l1.next = l11 = ListNode(1)
   l11.next = l12 = ListNode(2)
   l12.next = l13 = ListNode(4)
   l13.next = l14 = ListNode(4)
   S = Solution()
   res = S.deleteDuplicates(l1)
   while res:
       print(res.val)
       res = res.next


