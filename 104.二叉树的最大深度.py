#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (69.18%)
# Total Accepted:    49.8K
# Total Submissions: 72K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        递归获取
        '''
        if not root:
            return 0
        else :
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
            # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

if __name__ == "__main__":
   # 定义树
   l1 = TreeNode(-10)
   l1.left = l11 = TreeNode(9)
   l1.right = l12 = TreeNode(20)
   l12.left=l13=TreeNode(15)
   l12.right=l14=TreeNode(7)
   S = Solution()
   res = S.maxDepth(l1)
   print(res)
  

