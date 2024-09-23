class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        temp=0
        while i<j:
            temp=s[j]
            s[j]=s[i]
            s[i]=temp
            i+=1
            j-=1
------
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(n//2):
            s[-i-1],s[i]=s[i],s[-i-1]
            
        
        
