# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels=[]
        if root==None:
            return levels
        def dfs(node,level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        dfs(root,0)
        return levels
  ----
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels=[]
        if root==None:
            return levels
        level=0
        queue=deque([root])
        while queue:
            levels.append([])
            for i in range(len(queue)):
                node=queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return levels
        
