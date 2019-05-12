#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.52%)
# Total Accepted:    14.3K
# Total Submissions: 32.9K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst=[]
        Node=Head=ListNode(None)
        for eachLstNode in lists:
            while eachLstNode :
                lst.append(eachLstNode.val)
                eachLstNode=eachLstNode.next
        newLst=sorted(lst)
        for i in newLst:
            Head.next=ListNode(i)
            Head=Head.next
        return Node.next
                
# if __name__ == "__main__":    
#     L1 = None
#     L1 = ListNode(1)
#     L2 = ListNode(4)
#     L3 = ListNode(5)
#     L1.next = L2
#     L2.next = L3

#     L4 = None
#     L4 = ListNode(1)
#     L5 = ListNode(3)
#     L6 = ListNode(4)
#     L4.next = L5
#     L5.next = L6
    
#     L7 = None
#     L7 = ListNode(2)
#     L8 = ListNode(6)
#     L7.next = L8
#     lst=[L1,L4,L7]

#     S = Solution()
#     S.mergeKLists(lst)
