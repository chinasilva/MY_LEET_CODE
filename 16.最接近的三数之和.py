#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (39.52%)
# Total Accepted:    19.9K
# Total Submissions: 50.4K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        newNums = sorted(nums)
        res = sum(newNums[:3])
        for i in range(len(nums)-2):
            # print(res)
            l = i+1
            r = len(nums)-1
            #print(newNums)
            while l < r:
                sumNum = newNums[i]+newNums[l]+newNums[r]
                if target == sumNum:
                    return sumNum
                elif abs(res-target) > abs(sumNum-target):
                    res = sumNum
                elif target > sumNum:
                    l = l+1
                elif target < sumNum:
                    r = r-1
        return res


if __name__ == "__main__":
    s = Solution()
    # s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
    # s.threeSum([-1, 0, 1, 2, -1, -4])
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
