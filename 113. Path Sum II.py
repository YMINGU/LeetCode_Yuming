# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,node,remain,path,ans):
        if node==None:
            return
        path.append(node.val)
        if remain==node.val and not node.left and not node.right:
            ans.append(list(path))
        else:
            self.dfs(node.left,remain-node.val,path,ans)
            self.dfs(node.right,remain-node.val,path,ans)
        path.pop()
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans=[]
        self.dfs(root,targetSum,[],ans)
        return ans
        
