class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack=[]
        res=[]
        for item in heights[::-1]:
            popped=0
            while stack and stack[-1]<item:
                popped+=1
                stack.pop()
            if not stack:
                res.insert(0,popped)
            else:
                res.insert(0,popped+1)
            stack.append(item)
        return res
        
