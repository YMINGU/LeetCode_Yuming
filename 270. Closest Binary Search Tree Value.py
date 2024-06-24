# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans=root.val
        while root:
            if abs(target-root.val)<abs(target-ans):
                ans=root.val
            elif abs(target-root.val)==abs(target-ans):
                ans=min(ans,root.val)
            if root.val<target:
                root=root.right
            else:
                root=root.left
        return ans
  ---------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack=[root]
        ans=root.val
        while stack:
            node=stack.pop()
            if node==None:
                continue
            if abs(target-node.val)<abs(target-ans):
                ans=node.val
            elif abs(target-node.val)==abs(target-ans):
                ans=min(ans,node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
        
