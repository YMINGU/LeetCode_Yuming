# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        max_sum=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr,prev=slow,None
        while curr:
            curr.next,prev,curr=prev,curr,curr.next
        start=head
        while prev:
            max_sum=max(max_sum,start.val+prev.val)
            start=start.next
            prev=prev.next
        return max_sum
---
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr=head
        values=[]
        while curr:
            values.append(curr.val)
            curr=curr.next
        i=0
        j=len(values)-1
        max_sum=0
        while i<j:
            max_sum=max(max_sum,values[i]+values[j])
            i+=1
            j-=1
        return max_sum
        
        
