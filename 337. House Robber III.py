# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0,0)
            left=helper(node.left)
            right=helper(node.right)
            rob=node.val+left[1]+right[1]
            not_rob=max(left)+max(right)
            return [rob,not_rob]
        return max(helper(root))
  ----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob_saved={}
        not_rob_saved={}
        def helper(node,parent_robbed):
            if not node:
                return 0
            if parent_robbed:
                if node in rob_saved:
                    return rob_saved[node]
                result=helper(node.left,False)+helper(node.right,False)
                rob_saved[node]=result
                return result
            else:
                if node in not_rob_saved:
                    return not_rob_saved[node]
                rob=node.val+helper(node.left,True)+helper(node.right,True)
                not_rob=helper(node.left,False)+helper(node.right,False)
                result=max(rob,not_rob)
                not_rob_saved[node]=result
                return result
        return helper(root,False)
        
