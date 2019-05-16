#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.32%)
# Total Accepted:    35.5K
# Total Submissions: 65.1K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
#


class Solution:
    def maxArea(self, height) -> int:
       # 暴力解法，超时
       length = len(height)
       # tmp = 0
       # for i in range(length):
       #     for j in range(i+1, length):
       #         result = (j-i) * min(height[i], height[j])
       #         if tmp == 0 or result > tmp:
       #             tmp = result
       # #output = max(lst)
       # return tmp
       # return output
       
       #改进算法时间复杂度由O(N^2)降为O(N),max始终保留计算最大值
       l = 0
       r = length-1
       maxarea = 0
       while l < r:
           maxarea = max(maxarea, min(height[l], height[r])*(r-l))
           if height[l] < height[r]:
               l=l+1
           else:
                r=r-1
       return maxarea



if __name__ == "__main__":
    s = Solution()
    lst = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # lst = [1, 8]
    print(s.maxArea(lst))
