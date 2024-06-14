# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,curr):
            if node==None:
                return False
            if node.left==None and node.right==None:
                return (curr+node.val)==targetSum
            curr+=node.val
            left=dfs(node.left,curr)
            right=dfs(node.right,curr)
            return left or right
        return dfs(root,0)
------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        stack=[(root,0)]
        while stack:
            node,curr=stack.pop()
            if node.left==None and node.right==None:
                if (node.val+curr)==targetSum:
                    return True
            curr+=node.val
            if node.left:
                stack.append((node.left,curr))
            if node.right:
                stack.append((node.right,curr))
        return False
        
        
