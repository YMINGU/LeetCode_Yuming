class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        n=min([len(s) for s in strs])
        for i in range(n):
            j=0
            while j<len(strs):
                if strs[0][i]!=strs[j][i]:
                    break
                j+=1
                if j==len(strs):
                    ans.append(strs[0][i])
            if j!=len(strs):
                break
        return "".join(ans) if ans else ""
  ------
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)!=0:
                prefix=prefix[:len(prefix)-1]
                if prefix=="":
                    return ""
        return prefix
  -----
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==None or len(strs)==0:
            return ""
        for i in range(len(strs[0])):
            c=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=c:
                    return strs[0][0:i]
        return strs[0]
        
