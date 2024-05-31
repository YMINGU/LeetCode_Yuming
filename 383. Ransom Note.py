from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note=defaultdict(int)
        mag=defaultdict(int)
        for s in ransomNote:
            note[s]+=1
        for s in magazine:
            mag[s]+=1
        Flag=len(note)
        for key in note:
            if note[key]<=mag[key]:
                Flag-=1
        return True if Flag==0 else False
--------------------------------------------
