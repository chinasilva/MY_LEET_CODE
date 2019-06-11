#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (45.42%)
# Total Accepted:    51.1K
# Total Submissions: 112.4K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        动态规划方法,使用字典记录
        :type n: int
        :rtype: int
        """
        climb = dict()
        climb[0], climb[1] = 1, 1
        for i in range(2, n + 1):
            climb[i] = climb[i - 1] + climb[i- 2]

        return climb[n]
        # 递归方式，效率太低        
        # if n>2:
        #     return self.climbStairs(n-2)+self.climbStairs(n-1)
        # elif n==1:
        #     return 1
        # elif n==2:
        #     return 2

if __name__ == "__main__":
    s = Solution()
    # lst= [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
    #lst= [-2,1,-3,4,-1,2,1,-5,4]
    #  ,[1,2,3]
    print(s.climbStairs(28))
