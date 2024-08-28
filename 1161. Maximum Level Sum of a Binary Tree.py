from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum=float("-inf")
        ans=0
        level=0
        q=deque([root])
        while q:
            level+=1
            level_sum=0
            for _ in range(len(q)):
                node=q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum<level_sum:
                max_sum=level_sum
                ans=level
        return ans
---
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,level,level_sum):
            if node==None:
                return
            if len(level_sum)==level:
                level_sum.append(node.val)
            else:
                level_sum[level]+=node.val
            dfs(node.left,level+1,level_sum)
            dfs(node.right,level+1,level_sum)
        level_sum=[]
        dfs(root,0,level_sum)
        return 1+level_sum.index(max(level_sum))
        
