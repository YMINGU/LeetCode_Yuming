from collections import Counter
from heapq import *
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count=Counter(words)
        heap=[(-freq,word) for word,freq in count.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
        
