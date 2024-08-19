from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        c1=Counter(word1)
        c2=Counter(word2)
        if set(c2.keys())!=set(c1.keys()):
            return False
        if sorted(c1.values())!=sorted(c2.values()):
            return False
        return True
        
        
