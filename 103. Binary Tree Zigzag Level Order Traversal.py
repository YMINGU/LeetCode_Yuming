# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret=[]
        level_list=deque()
        if root == None:
            return []
        node_queue=deque([root,None])
        is_order_left=True
        while node_queue:
            curr_node=node_queue.popleft()
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                ret.append(level_list)
                if node_queue:
                    node_queue.append(None)
                level_list=deque()
                is_order_left=not is_order_left
        return ret
        
