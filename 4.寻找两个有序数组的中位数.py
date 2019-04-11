#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (34.02%)
# Total Accepted:    43.8K
# Total Submissions: 128.1K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#
# import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        :nums1: List[int],
        :nums2: List[int]
        '''
        
        myList=nums1+nums2
        # myList.sort(reverse=False)
        # median= np.median(myList)
        median=self.getMedian(myList)
        return median

    def getMedian(self,data):
        data=sorted(data)
        size=len(data)
        if size % 2 ==0: #偶数个
            median=(data[size//2]+data[size//2-1])/2
            return median 
        else:
            median=data[(size-1)//2]
            return median

# if __name__=="__main__":
#     sl= Solution()
#     ret= sl.findMedianSortedArrays([123,1234],[456])


