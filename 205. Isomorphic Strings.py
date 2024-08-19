
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}
        t_s={}
        for c1,c2 in zip(s,t):
            if c1 not in s_t and c2 not in t_s:
                s_t[c1]=c2
                t_s[c2]=c1
            elif s_t.get(c1)!=c2 or t_s.get(c2)!=c1:
                return False
        return True

----
class Solution:
    def trans(self,s:str)->str:
        index={}
        new_str=[]
        for i,c in enumerate(s):
            if c not in index:
                index[c]=i
            new_str.append(str(index[c]))
        return " ".join(new_str)
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.trans(s)==self.trans(t)
        
        
