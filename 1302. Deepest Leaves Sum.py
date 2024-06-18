# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            length=len(queue)
            currmax=float("-inf")
            for _ in range(length):
                node=queue.popleft()
                currmax=max(currmax,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currmax)
        return ans
-------------
