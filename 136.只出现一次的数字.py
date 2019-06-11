#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (61.38%)
# Total Accepted:    72.4K
# Total Submissions: 118K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#
class Solution:
    def singleNumber(self, nums) -> int:
        # dic=dict()
        
        # for i in range(len(nums)):
        #     if nums[i] in nums:
        #         nums[i]=1
        # if len(nums)==0:
        #     return 0
        nums=sorted(nums)  
        for i in range(0,len(nums),2):
            if i==len(nums)-1 or nums[i]!=nums[i+1]: #最后一位
                return nums[i]
        # .sor    
if __name__=="__main__":
    s=Solution()
    print(s.singleNumber([4,1,2,1,2]))