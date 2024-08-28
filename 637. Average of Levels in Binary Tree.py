from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        avg = []
        cur = [root]
        while cur:
            next_ = []
            mean = 0.0
            for node in cur:
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
                mean += node.val
            avg.append(mean / len(cur))
            cur = next_
        return avg
        
  ------
