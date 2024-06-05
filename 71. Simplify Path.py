class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for c in path.split('/'):
            if c=='..':
                if stack:
                    stack.pop()
            elif c=='.' or not c:
                continue
            else:
                stack.append(c)
        return "/"+"/".join(stack)
        
