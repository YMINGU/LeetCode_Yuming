# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        def bs(target,seen):
            left=0
            right=len(seen)-1
            while left<right:
                mid=(left+right)//2
                if target==seen[mid]:
                    return [target,target]
                elif target>seen[mid]:
                    left=mid+1
                else:
                    right=mid
            if target==seen[left]:
                return [target,target]
            elif left==len(seen)-1 and target>seen[left]:
                return [seen[left],-1]
            elif left==0 and target<seen[left]:
                return [-1,seen[left]]
            else:
                return [seen[left-1],seen[left]]
        seen=[]
        def dfs(curr):
            if curr is None:
                return 
            dfs(curr.left)
            seen.append(curr.val)
            dfs(curr.right)
        dfs(root)
        return [bs(i,seen) for i in queries]
     
                
        
