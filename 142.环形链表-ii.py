#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # fast每次走两步，slow每次走一步，根据龟兔同圈赛跑，有环一定追上
        # 无环返回None
        # 假设ABC三点，A为起始点，B为环入口点，C为交点，A至B距离为x，B至C距离为y，C至B距离为z
        # 距离公式为：x+y+z+y=2*（x+y）,化简得x=z。此时两个指针在交点C，头指针和slow指针都走
        # x或z步(x=z)，交点即环入口点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow2 = head
                # index=0
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                    
                return slow
        return None

# if __name__ == "__main__":
#    L1 = None
#    L1 = ListNode(3)
#    L2 = ListNode(2)
#    L3 = ListNode(0)
#    L4 = ListNode(-4)
# #    L5 = ListNode(4)
#    L1.next = L2
#    L2.next = L3
#    L3.next = L4
#    L4.next = L2


#    S = Solution()
#    print(S.detectCycle(L1))
  



