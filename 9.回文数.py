#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (55.84%)
# Total Accepted:    105.8K
# Total Submissions: 189.1K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag=True # 循环内标志位
        tmpStr= str(x)
        tmpStrLen= len(tmpStr)
        if x<0:
            return False
        elif tmpStrLen%2==0: # 偶数
            L=tmpStrLen//2-1
            R=tmpStrLen//2
            while L >=0:
                if tmpStr[L]!=tmpStr[R]:
                    flag=False
                    break
                L=L-1
                R=R+1
        else : #奇数
            L=tmpStrLen//2-1
            R=tmpStrLen//2+1
            while L >=0:
                if tmpStr[L]!=tmpStr[R]:
                    flag=False
                    break
                L=L-1
                R=R+1
        if flag:
            return True
        else :
            return False

# if __name__=="__main__":
#     sl= Solution()
#     print(sl.isPalindrome(123521))

