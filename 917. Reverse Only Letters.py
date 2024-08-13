class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans=[]
        j=len(s)-1
        for i,x in enumerate(s):
            if x.isalpha():
                while not s[j].isalpha():
                    j-=1
                ans.append(s[j])
                j-=1
            else:
                ans.append(x)
        return "".join(ans)
        
