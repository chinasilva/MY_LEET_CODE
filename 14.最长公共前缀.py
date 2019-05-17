#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.94%)
# Total Accepted:    52.7K
# Total Submissions: 164.7K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strsLen = len(strs)
        minLen = 2**31
        if strsLen == 0:
            return ""
        elif strsLen == 1:
            return strs[0]
        # 求出最小字符串长度,i+1为后一位，故循环至:strsLen-1
        for i in range(strsLen-1):
            minLen = min(minLen,min(len(strs[i]), len(strs[i+1]))) 

        # 双重循环,
        for i in range(strsLen-1):
            for j in range(minLen):
                if strs[i][j] != strs[i+1][j]:
                    minLen = j #-1
                    break
        if minLen > 0:
            return strs[0][0:minLen]
        else:
            return ""


if __name__ == "__main__":
    s = Solution()
    # print(s.longestCommonPrefix( ["flower","flow","flight"]))
    # print(s.longestCommonPrefix( ["aa","ab"]))
    # print(s.longestCommonPrefix( ["a",""]))
    # print(s.longestCommonPrefix( []))
    # print(s.longestCommonPrefix( ["a"]))
    print(s.longestCommonPrefix( ["caa","","a","acb"]))
    # ["caa","","a","acb"]
