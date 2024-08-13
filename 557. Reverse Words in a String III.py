class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        left,right=0,0
        s+=" "
        while left<len(s):
            while right<len(s)-1 and s[right]!=" ":
                right+=1
            res+=s[left:right+1][::-1]
            left=right+1
            right=left
        return res[1:]
        
