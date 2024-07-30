class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, i):
            if len(curr)== n:
                ans.add(int("".join(curr)))
                return 
            if i+k <10:
                curr.append(str(i+k))
                backtrack(curr,i+k)
                curr.pop()
            if i-k >-1:
                curr.append(str(i-k))
                backtrack(curr,i-k)
                curr.pop()
            
        ans =set()
        for h in range(1,10):
            backtrack([str(h)],h)
        return ans
