class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class MyLinkedList(object):
    def __init__(self):
        self.size=0
        self.head=ListNode(0)
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index <0 or index >=self.size:
            return -1
        curr=self.head
        for _ in range(index+1):
            curr=curr.next
        return curr.val
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size:
            return
        if index<0:
            index=0
        self.size+=1
        pred=self.head
        for _ in range(index):
            pred=pred.next
        to_add=ListNode(val)
        to_add.next=pred.next
        pred.next=to_add
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return
        self.size-=1
        pred=self.head
        for _ in range(index):
            pred=pred.next
        pred.next=pred.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
