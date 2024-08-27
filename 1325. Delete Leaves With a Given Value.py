# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        root.left=self.removeLeafNodes(root.left,target)
        root.right=self.removeLeafNodes(root.right,target)
        if root.left is None and root.right is None and root.val==target:
            return None
        return root
---------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        stack=[]
        curr=root
        last_right=None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack[-1]
            if curr.right and curr.right is not last_right:
                curr=curr.right
                continue
            stack.pop()
            if not curr.right and not curr.left and curr.val==target:
                if not stack:
                    return None
                parent=stack[-1] if stack else None
                if parent and parent.left is curr:
                    parent.left=None
                elif parent and parent.right is curr:
                    parent.right=None
            last_right=curr
            curr=None
        return root
        
