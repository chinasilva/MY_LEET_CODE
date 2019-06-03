#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (38.25%)
# Total Accepted:    15.8K
# Total Submissions: 41.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        Lst=head
        #考虑到链表中next为空,初始化长度给1
        LstLength=1
        while Lst.next:
            Lst=Lst.next
            LstLength +=1
        else: #组成环
            Lst.next=head
        # Lst=head
        #确定首位元素
        # firstNode=(abs(LstLength-k)+1) if (LstLength-k)<0 else (LstLength-k)
        firstNode=k%LstLength
        for i in range(firstNode):
            Lst=Lst.next
        Lst=Lst.next
        #拆除环
        head=Lst
        for i in range(LstLength-1):
            Lst=Lst.next
        Lst.next=None
        return head


if __name__ == "__main__":

   L1 = None
   L1 = ListNode(1)
   L2 = ListNode(4)
   L3 = ListNode(5)
   L1.next = L2
   L2.next = L3

   S = Solution()
   L3 = S.rotateRight(L1, 4)
   while L3:
       print(L3.val)
       L3=L3.next


# × 44/231 cases passed (N/A)
#   × testcase: '[1,2,3,4,5]\n2'
#   × answer: [3,4,5,1,2]
#   × expected_answer: [4,5,1,2,3]
#   × stdout: 4
# 5

