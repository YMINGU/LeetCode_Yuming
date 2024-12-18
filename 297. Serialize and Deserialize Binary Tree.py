# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root,string):
            if root is None:
                string+="None,"
            else:
                string+=str(root.val)+","
                string=dfs(root.left,string)
                string=dfs(root.right,string)
            return string
        return dfs(root,"")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(l):
            if l[0]=="None":
                l.pop(0)
                return None
            root=TreeNode(l[0])
            l.pop(0)
            root.left=dfs(l)
            root.right=dfs(l)
            return root
        data_list=data.split(",")
        root=dfs(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
