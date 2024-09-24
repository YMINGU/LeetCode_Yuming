from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        ans=[]
        for l in count.values():
            if len(l)==1:
                ans.append(l[0])
        return min(ans) if ans else -1
-------
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for idx,ch in enumerate(s):
            if count[ch]==1:
                return idx
        return -1
        
