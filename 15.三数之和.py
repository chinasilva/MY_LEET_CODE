#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (21.50%)
# Total Accepted:    43.3K
# Total Submissions: 200.7K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums):
        # 三次循环 O(N^3)
        # lst=[]
        # for a in range(len(nums)):
        #     for b in range(a+1,len(nums)):
        #         for c in range(b+1,len(nums)):
        #             if nums[a]+nums[b]+nums[c]==0:
        #                 mylst=[nums[a],nums[b],nums[c]]
        #                 mylst.sort()
        #                 if mylst in lst:
        #                     break
        #                 else:
        #                     lst.append(mylst)
        #                 lst.append(mylst)
        # return ret
        
        #一次循环，从两头进行求和 O(N^2)
        lst=[]
        nums.sort()
        numlen=len(nums)
        for a in range(numlen-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            left=a+1
            right=numlen-1
            while left<right:
                sum=nums[a]+nums[left]+nums[right]
                if sum>0:
                    right=right-1
                elif sum<0:
                    left=left+1
                else:
                    lst.append([nums[a],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-+1
                    # mylist=[nums[a],nums[left],nums[right]]
                    # left=left+1
                    # right=right-1
                    # if mylist not in lst:
                    #     lst.append(mylist)
        return lst

    # def threeSum(self, nums):
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)-2):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         l, r = i+1, len(nums)-1
    #         while l < r:
    #             s = nums[i] + nums[l] + nums[r]
    #             if s < 0:
    #                 l +=1 
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 res.append((nums[i], nums[l], nums[r]))
    #                 while l < r and nums[l] == nums[l+1]:
    #                     l += 1
    #                 while l < r and nums[r] == nums[r-1]:
    #                     r -= 1
    #                 l += 1; r -= 1
    #     return res

# if __name__=="__main__":
#     s=Solution()
#     # s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
#     # s.threeSum([-1, 0, 1, 2, -1, -4])
#     s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    
