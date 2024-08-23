class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j=0
        stack=[]
        for x in pushed:
            stack.append(x)
            while stack and j<len(popped) and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return j==len(popped)
        
