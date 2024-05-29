from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts=defaultdict(int)
        for s in text:
            counts[s]+=1
        return min(counts['a'],counts['b'],int(counts['l']/2),int(counts['o']/2),counts['n'])
----------------------------------------------------------------------------------------------
