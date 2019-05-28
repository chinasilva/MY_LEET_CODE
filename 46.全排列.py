#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (68.86%)
# Total Accepted:    25.5K
# Total Submissions: 36.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
import itertools


class Solution:
    # def permute(self, nums):
    #     # 使用python 全排列类库进行操作
    #     lst=list(itertools.permutations(nums,len(nums))) 
    #     for i in range(len(lst)):
    #         lst[i]=list(lst[i])
    #     return lst

    # DFS 递归进行遍历
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

if __name__ == "__main__":
    s = Solution()
    lst=[1,2,3]
    print(s.permute(lst))