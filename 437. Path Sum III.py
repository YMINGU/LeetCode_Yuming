# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.count=0
        def dfs(node,res):
            if not node:
                return None
            if node.val==targetSum:
                self.count+=1
            for i in range(len(res)):
                res[i]+=node.val
                if res[i]==targetSum:
                    self.count+=1
            dfs(node.left,res+[node.val])
            dfs(node.right,res+[node.val])
        dfs(root,[])
        return self.count
        
