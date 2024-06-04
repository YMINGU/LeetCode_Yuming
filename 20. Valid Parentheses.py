class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matching={'(':')','{':'}','[':']'}
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                curr=stack.pop()
                if matching[curr]!=c:
                    return False
        return not stack
                    
        
