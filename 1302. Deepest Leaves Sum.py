# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        queue=deque([(root,0)])
        ans=0
        depth=0
        while queue:
            length=len(queue)
            for _ in range(length):
                node,curr=queue.popleft()
                if node.left==None and node.right==None:
                    if depth<curr:
                        ans=node.val
                        depth=curr
                    elif depth==curr:
                        ans+=node.val
                    
                else:
                    if node.left:
                        queue.append((node.left,curr+1))
                    if node.right:
                        queue.append((node.right,curr+1))
        return ans
                    
        
        
