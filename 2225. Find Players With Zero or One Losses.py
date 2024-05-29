from collections import defaultdict 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        countslose=defaultdict(int)
        countswin=defaultdict(int)
        nonlose=[]
        onelose=[]
        for arr in matches:
            countswin[arr[0]]+=1
            countslose[arr[1]]+=1
        for key in countslose:
            if countslose[key]==1:
                onelose.append(key)
        for key in countswin:
            if key not in countslose:
                nonlose.append(key)
        return [sorted(nonlose),sorted(onelose)]


------------------------------------------------------------------------------

from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counts=defaultdict(int)
        nonlose=[]
        onelose=[]
        for winner, loser in matches:
            if winner not in counts:
                counts[winner]=0
            counts[loser]+=1
        for key in counts:
            if counts[key]==0:
                nonlose.append(key)
            if counts[key]==1:
                onelose.append(key)
        return [sorted(nonlose),sorted(onelose)]
        
        
        
        
        
