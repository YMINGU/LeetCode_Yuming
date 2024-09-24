class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars=filter(lambda ch:ch.isalnum(),s)
        lowercase_filtered_chars=map(lambda ch: ch.lower(),filtered_chars)
        a=list(lowercase_filtered_chars)
        b=a[::-1]
        return a==b
  -----
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        
