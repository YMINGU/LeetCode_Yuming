class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        alphabet=set(alpha)
        sen_set=set(sentence)
        for a in alphabet:
            if a not in sen_set:
                return False
            else:
                continue
        return True

-----

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen=set(sentence)
        return len(seen)==26
        
        
