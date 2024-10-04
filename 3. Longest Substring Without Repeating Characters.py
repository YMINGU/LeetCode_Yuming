class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        charnext={}
        i=0
        for j in range(n):
            if s[j] in charnext:
                i=max(charnext[s[j]],i)
            ans=max(ans,j-i+1)
            charnext[s[j]]=j+1
        return ans
        
