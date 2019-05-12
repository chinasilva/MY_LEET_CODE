#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (24.96%)
# Total Accepted:    55.5K
# Total Submissions: 222.1K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen=len(s)
        if sLen==0 or sLen==1:
            print (s)
            return s
        lst=[]
        self.common(s,1,lst)
        self.common(s,2,lst) 
        if len(lst)<=0:
            return s[0]
        newLst=sorted(lst,key=len,reverse=True)
        # 多种输出，此题不需要故不用考虑，直接返回最大的任意一值
        # maxLen=len(newLst[0])
        # for i in newLst:
        #     if len(i)==maxLen :
        #         print (i)
        #         return i
        return newLst[0]


    def common(self,s,nTpye,lst):
        r"""
        nTpye : =1 两数回文相连 12344321
                =2 两数回文有间隔 12345321
        """
        sLen=len(s)
        for i in range(sLen):
            L=i
            R=i+nTpye
            # R=sLen-1
            while L>=0 and R<sLen and s[L]==s[R]:
                lst.append(s[L:R+1])
                # tmp=
                L=L-1 
                R=R+1
# if __name__=="__main__":
#     sl= Solution()
#     sl.longestPalindrome('babad')

