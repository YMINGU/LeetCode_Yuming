class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s="".join(s.split("-"))
        s=s.upper()[::-1]
        ans=[]
        for i in range(len(s)):
            if i%k==0 and i!=0:
                ans.append("-")
            ans.append(s[i])
        return "".join(ans)[::-1]
------
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n=len(s)
        count=0
        ans=[""]
        for i in reversed(range(n)):
            if s[i]!="-":
                ans+=s[i].upper()
                count+=1
                if count==k:
                    count=0
                    ans+='-'
        if len(ans)>0 and ans[len(ans)-1]=="-":
            ans=ans[:-1]
        return "".join(ans)[::-1]
        
