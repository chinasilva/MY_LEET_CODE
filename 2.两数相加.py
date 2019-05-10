#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.59%)
# Total Accepted:    85.8K
# Total Submissions: 263.2K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)
        n=root # n为链表,root为第一个节点
        str1=''
        str2=''
        while l1:
            str1+=(str(l1.val))
            l1=l1.next
        while l2:
            str2+=(str(l2.val))
            l2=l2.next
        str1=str1[::-1]
        str2=str2[::-1]
        num1=int(str1)
        num2=int(str2)
        sum=num1+num2
        lstNum=list(str(sum))
        lstNum.reverse()
        for i in range(len(lstNum)):
            root.next=ListNode(lstNum[i])
            if root.next is not None:
                root=root.next
        return n.next

# if __name__ == "__main__":

#    L1 =ListNode(2) 
#    L1.next= ListNode(4)
#    L1.next.next=ListNode(3)
#    L2 =ListNode(5) 
#    L2.next= ListNode(6)
#    L2.next.next=ListNode(4)
#    S = Solution()
#    L3 = S.addTwoNumbers(L1, L2)
#    while L3:
#        print(L3.val)
#        L3=L3.next
#   # s.addTwoNumbers()
