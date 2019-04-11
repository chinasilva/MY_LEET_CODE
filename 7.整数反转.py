#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.59%)
# Total Accepted:    89K
# Total Submissions: 280.2K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
# class Solution:
#     def reverse(self, x: int) -> int:
#         length=0
#         numflag=1
#         result=''
#         if x<0:
#             length=len(str(x))-1
#             numflag=-1
#             x=x*numflag
#         else:
#             length=len(str(x))
#         for i in range(length):
#             y=int(x/pow(10,length-i-1))
#             result=result +str(y)
#             x=int(x%pow(10,length-i-1))
#         result=result[::-1]
#         return int(result)*numflag


# list[<start>:<stop>:<step>]
class Solution:
    def reverse(self, x: int) -> int:
        numflag=1
        result=''
        if x<0:
            numflag=-1
            x=x*numflag
        result=str(x)
        result=result[::-1]
        if int(result)>pow(2,31):
            result=0
        return int(result)*numflag


# if __name__=="__main__":
#     s=Solution()
#     ret= s.reverse(-900000)
#     print(ret)
