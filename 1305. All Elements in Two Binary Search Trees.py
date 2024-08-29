from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def getlist(root):
            if root==None:
                return []
            queue=deque([root])
            nodes=[root.val]
            while queue:
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    nodes.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    nodes.append(node.right.val)
            return nodes
        list1=getlist(root1)
        list2=getlist(root2)
        ans=list1+list2
        return sorted(ans)
                
  ----
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(r):
            return inorder(r.left)+[r.val]+inorder(r.right) if r else []
        return sorted(inorder(root1)+inorder(root2))
  ----
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        stack1,stack2,output=[],[],[]
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1=root1.left
            while root2:
                stack2.append(root2)
                root2=root2.left
            if not stack2 or stack1 and stack1[-1].val<=stack2[-1].val:
                root1=stack1.pop()
                output.append(root1.val)
                root1=root1.right
            else:
                root2=stack2.pop()
                output.append(root2.val)
                root2=root2.right
        return output
        
