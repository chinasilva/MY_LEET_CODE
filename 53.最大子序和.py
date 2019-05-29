#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.92%)
# Total Accepted:    58.6K
# Total Submissions: 129.9K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#
class Solution:
    def maxSubArray(self, nums) -> int:
        # #动态规划方法，不断去更新最大值
        # sumNum=0
        # maxNum=0
        # lstLen=len(nums)
        # for i in range(lstLen):
        #     sumNum+=nums[i]
        #     if sumNum>maxNum:
        #         maxNum=sumNum
        #     elif sumNum<0: # 和小于0则当成0看，选择下一个进行求和
        #         sumNum=0
        # if maxNum==0: #对于全负的进行最值选取
        #     maxNum=max(nums)
        # return maxNum

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num) #选取当前值和当前所有前向最大值
            maxSum = max(maxSum, curSum)

        return maxSum

if __name__ == "__main__":
    s = Solution()
    lst= [-2,-3]
    #lst= [-2,1,-3,4,-1,2,1,-5,4]
    #  ,[1,2,3]
    print(s.maxSubArray(lst))

