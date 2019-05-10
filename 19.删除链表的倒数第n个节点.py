#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.36%)
# Total Accepted:    42.1K
# Total Submissions: 126.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        LinkLst=head
        # posLst=ListNode(0) 
        length=1
        while head.next:
            length+=1
            posLst=head # posLst占位节点
            head=head.next
        diffNum=length-n
        
            


if __name__ == "__main__":
   L1 =ListNode(2) 
   L1.next= ListNode(4)
   L1.next.next=ListNode(3)
#    L2 =ListNode(5) 
#    L2.next= ListNode(6)
#    L2.next.next=ListNode(4)
   S = Solution()
   L3 = S.removeNthFromEnd(L1, 3)
   while L3:
       print(L3.val)
       L3=L3.next
  # s.addTwoNumbers()

