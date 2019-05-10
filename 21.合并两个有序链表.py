#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (54.17%)
# Total Accepted:    64.8K
# Total Submissions: 119.6K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # 递归方式
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # merged_head = None
        # if(l1.val <= l2.val):
        #     merged_head = l1
        #     merged_head.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     merged_head = l2
        #     merged_head.next = self.mergeTwoLists(l1, l2.next)
        # return merged_head
        
        # 普通方式 
        l3=[]
        l4 = ListNode(0)
        merged_head = l4
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         l3.append(l1.val)
        #         l1 = l1.next
        #     else:
        #         l3.append(l2.val)
        #         l2 = l2.next
        while l1:
            l3.append(l1.val)
            l1=l1.next
        while l2:
            l3.append(l2.val)
            l2=l2.next
        l3.sort()
        for i in range(len(l3)):
            l4.next=ListNode(l3[i])
            l4=l4.next
        return merged_head.next

        # # 普通方式,不使用list
        # merged_list = ListNode(0)
        # merged_head = merged_list

        # # Scan through l1 and l2, get the smaller one to merged list
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         merged_list.next = l1
        #         l1 = l1.next
        #     else:
        #         merged_list.next = l2
        #         l2 = l2.next
        #     merged_list = merged_list.next

        # # l2 has gone to the tail already and only need to scan l1
        # while l1:
        #     merged_list.next = l1
        #     l1 = l1.next
        #     merged_list = merged_list.next

        # # l1 has gone to the tail already and only need to scan l2
        # while l2:
        #     merged_list.next = l2
        #     l2 = l2.next
        #     merged_list = merged_list.next

        # return merged_head.next

# if __name__ == "__main__":
#    # 定义l1链表
#    l1 = ListNode(1)
#    l1.next = l11 = ListNode(2)
#    l11.next = l12 = ListNode(4)
#    # 定义l2链表
#    l2 = ListNode(1)
#    l2.next = l21 = ListNode(3)
#    l21.next = l22 = ListNode(4)
#    S = Solution()
#    res = S.mergeTwoLists(l1, l2)
#    while res:
#        print(res.val)
#        res = res.next