# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev=[]
        def dfs(curr,level):
            if curr==None:
                return True
            if curr.val%2==level%2:
                return False
            while len(prev)<=level:
                prev.append(0)
            if prev[level]!=0 and ((level%2==0 and curr.val<=prev[level]) or (level%2==1 and curr.val>=prev[level])):
                return False
            prev[level]=curr.val
            return dfs(curr.left,level+1) and dfs(curr.right,level+1)
        curr=root
        return dfs(curr,0)
  -----
