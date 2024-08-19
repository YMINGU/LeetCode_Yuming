class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=Counter(s)
        result=""
        for i in order:
            result+=count[i]*i
            del(count[i])
        for i,j in count.items():
            result+=i*j
        return result
        
