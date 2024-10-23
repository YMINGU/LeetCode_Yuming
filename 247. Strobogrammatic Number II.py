class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        rever_pairs=[['0','0'],['1','1'],['6','9'],['8','8'],['9','6']]
        string_length=n%2
        q=["0","1","8"] if string_length==1 else [""]
        while string_length<n:
            string_length+=2
            next_level=[]
            for num in q:
                for pair in rever_pairs:
                    if string_length!=n or pair[0]!="0":
                        next_level.append(pair[0]+num+pair[1])
                q=next_level
        return q
        
