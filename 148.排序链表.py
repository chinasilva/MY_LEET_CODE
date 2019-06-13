#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        newNode=node=head
        lst=[]
        while node:
            lst.append(node.val)
            node=node.next         
        lst=sorted(lst)
        for i in lst:
            newNode.val=i
            newNode=newNode.next
        return head
# if __name__ == "__main__":

#    L1 = None
#    L1 = ListNode(1)
#    L2 = ListNode(4)
#    L3 = ListNode(5)
#    L4 = ListNode(4)
#    L5 = ListNode(5)
#    L1.next = L2
#    L2.next = L3
#    L3.next = L4
#    L4.next = L5


#    S = Solution()
#    L3 = S.sortList(L1)
#    while L3:
#        print(L3.val)
#        L3=L3.next

