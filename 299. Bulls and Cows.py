from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h=defaultdict(int)
        bulls=cows=0
        for i,s in enumerate(secret):
            g=guess[i]
            if s==g:
                bulls+=1
            else:
                cows+=int(h[s]<0)+int(h[g]>0)
                h[s]+=1
                h[g]-=1
        return "{}A{}B".format(bulls,cows)
        
