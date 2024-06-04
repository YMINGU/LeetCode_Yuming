class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1]==c:
                stack.pop(-1)
            else:
                stack.append(c)
        return "".join(stack)
        
