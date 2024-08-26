# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root,arr):
            if not root:
                return arr
            elif not root.left and not root.right:
                arr.append(root.val)
                return arr
            else:
                arr=dfs(root.left,arr)
                arr=dfs(root.right,arr)
                return arr
        return dfs(root1,[])==dfs(root2,[])
        
