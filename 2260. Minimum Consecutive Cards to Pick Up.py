from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic=defaultdict(list)
        ans=float("inf")
        for i in range(len(cards)):
            dic[cards[i]].append(i)
        for key in dic:
            for i in range(1,len(dic[key])):
                ans=min(ans,dic[key][i]-dic[key][i-1]+1)
        return ans if ans<float("inf") else -1

  ----------------------------------------------------------

from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic=defaultdict(list)
        ans=float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans=min(ans,i-dic[cards[i]]+1)
            dic[cards[i]]=i
        return ans if ans<float("inf") else -1
        
