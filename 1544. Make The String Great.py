class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack[-1]!=c+32 or stack[-1]==c-32:
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)
        
