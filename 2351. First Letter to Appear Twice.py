class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j]:
                    return s[i]
        return -1

-----

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return ""
        
