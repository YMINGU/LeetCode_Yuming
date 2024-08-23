class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                diff=stack[-1]+a
                if diff<0:
                    stack.pop()
                elif diff>0:
                    a=0
                else:
                    stack.pop()
                    a=0
            if a:
                stack.append(a)
        return stack
        
