# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=node=head
        number=2
        node=node.next
        while node:
            li=[]
            num=number
            temp=node
            while node and num>0:
                li.append(node.val)
                node=node.next
                num-=1
            if len(li)%2==0:
                for rev_node_val in li[::-1]:
                    temp.val=rev_node_val
                    temp=temp.next
            number+=1
        return prev
