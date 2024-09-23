class Solution:
    def reverse(self, x: int) -> int:
        string=str(x)
        pos=True
        if string[0]=="-":
            string=string[1:]
            pos=False
        string=list(string)
        for i in range(len(string)//2):
            string[-i-1],string[i]=string[i],string[-i-1]
        d=int("".join(string))
        if pos:
            return d if -2**31<=d<=2**31-1 else 0
        else:
            return -d if -2**31<=-d<=2**31-1 else 0
            
            
  -----
class Solution:
    def reverse(self, x: int) -> int:
        ans=int(str(abs(x))[::-1])*(-1 if x<0 else 1)
        return ans if -2**31<=ans<=2**31-1 else 0
        
