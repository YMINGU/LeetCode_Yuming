class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        minimum=s[-1]
        for i in range(len(s)-2,-1,-1):
            if s[i]<minimum[-1]:
                minimum+=s[i]
            else:
                minimum+=minimum[-1]
        minimum=minimum[::-1]
        stack=[]
        res=""
        for i in range(len(s)):
            while stack and stack[-1]<=minimum[i]:
                res+=stack.pop()
            stack.append(s[i])
        return res+"".join(stack[::-1])
----
