#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (72.71%)
# Total Accepted:    10.1K
# Total Submissions: 13.9K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
class Solution:
    def generateMatrix(self, n: int):
        # lst=[[n*n]]
        # print([range(0,5)]+ [4])

        
        # A, lo = [], n*n+1
        # while lo > 1:
        #     lo, hi = lo - len(A), lo
        #     A = [range(lo, hi)] +  [*zip(*A[::-1])]
        #     print("tmp:",A)
        # print(A)
        # return A


        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
        

if __name__ == "__main__":
    s = Solution()
    # lst= [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
    #lst= [-2,1,-3,4,-1,2,1,-5,4]
    #  ,[1,2,3]
    print(s.generateMatrix(3))


