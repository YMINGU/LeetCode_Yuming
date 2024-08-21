# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals=[]
        curr=head
        while curr is not None:
            vals.append(curr.val)
            curr=curr.next
        return vals==vals[::-1]
----
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.front=head
        def check(curr=head):
            if curr is not None:
                if not check(curr.next):
                    return False
                if self.front.val!=curr.val:
                    return False
                self.front=self.front.next
            return True
        return check()
        
