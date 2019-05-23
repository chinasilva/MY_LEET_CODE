#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.04%)
# Total Accepted:    75.4K
# Total Submissions: 198K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#


class Solution:
    # def __init__(self):
        # self.dic = {'[': -1, '{': -2, '(': -3, ']': 1, '}': 2, ')': 3}

    # def isValid(self, s: str) -> bool:
    #     # s=set(s)
    #     sLen = len(s)
    #     # print(self.dic[s[0]])
    #     if sLen % 2 != 0:  # 奇数个数则错误
    #         return False
    #     if self.fun1(s) or self.fun2(s):
    #         return True
    #     else:
    #         return False

    # def fun1(self, s) -> bool:
    #     '''
    #     # 从中间向两边d移动
    #     '''
    #     sLen = len(s)
    #     L = sLen // 2 - 1
    #     R = sLen//2
    #     while R < sLen:
    #         # print(s[L])
    #         if self.dic[s[L]]+self.dic[s[R]] != 0:
    #             return False
    #         L = L-1
    #         R = R+1
    #     return True

    # def fun2(self, s) -> bool:
    #     '''
    #     # 从左向右移动
    #     '''
    #     sLen = len(s)
    #     for i in range(0, sLen, 2):
    #         L = i
    #         R = i+1
    #         if self.dic[s[L]]+self.dic[s[R]] != 0:
    #             return False
    #     return True

    def isValid(self, s):
        #定义一个空栈，如果开始的元素为括号左侧则进行入栈操作,
        #如果不在，则进行出栈操作，栈为空或者出栈元素不匹配则括号有问题,
        #所有栈内元素完成出栈操作
        stack,match=[],{"}":"{", "]":"[", ")":"("}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop()==match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack

if __name__ == "__main__":
    s = Solution()
  #  str0 = "()"
  #  str0 = "()[]{}"
   # str0 = "(]"
#    str0 = "([)]"
    str0 = "{[]}"
    # str0 = "["
    # str0="(([]){})"

    print(s.isValid(str0))
