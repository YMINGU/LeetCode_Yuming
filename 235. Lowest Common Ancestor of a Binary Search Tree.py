# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent=root
        if p.val>parent.val and q.val>parent.val:
            return self.lowestCommonAncestor(parent.right,p,q)
        elif p.val<parent.val and q.val<parent.val:
            return self.lowestCommonAncestor(parent.left,p,q)
        else:
            return parent
---------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node=root
        while node:
            parent=node
            if p.val>parent.val and q.val>parent.val:
                node=node.right
            elif p.val<parent.val and q.val<parent.val:
                node=node.left
            else:
                return node
        
