class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hash1={}
        hash2={}
        sub_len=0
        for char in s1:
            hash1[char]=hash1.get(char,0)+1
        for i,char in enumerate(s2):
            hash2[char]=hash2.get(char,0)+1
            while hash2[char]>hash1.get(char,0):
                hash2[s2[i-sub_len]]-=1
                sub_len-=1
            sub_len+=1
            if sub_len==len(s1):
                return True
        return False
            
        
