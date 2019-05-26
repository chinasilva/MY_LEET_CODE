#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.57%)
# Total Accepted:    25K
# Total Submissions: 68.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#
class Solution:
    def search(self, nums, target) -> int:
        # newNums=sorted(nums)
        numLength=len(nums)
        left=0
        right=numLength-1
        while left<=right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # 使用二分查找法进行两次调整
            # 1.调整原列表的排序
            # 2.调整查找中的排序    
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 # not found
 
if __name__ == "__main__":
    s = Solution()
    # nums=[4,5,6,7,0,1,2]#[1,1,2,2,3]
    nums=[]#[1,1,2,2,3]
    target=7
    print(s.search(nums,target))

