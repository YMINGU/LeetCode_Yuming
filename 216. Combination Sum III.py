class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr,i):
            if sum(curr)==n and len(curr)==k:
                ans.append(curr[:])
                return
            for h in range(i,10):
                if sum(curr)+h<=n:
                    curr.append(h)
                    backtrack(curr,h+1)
                    curr.pop()
        ans=[]
        backtrack([],1)
        return ans
                
  -----
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain - i - 1, comb, i + 1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results
    ------
    class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remain,curr,next_start):
            if remain==0 and len(curr)==k:
                ans.append(curr[:])
                return
            for i in range(next_start,10):
                curr.append(i)
                backtrack(remain-i,curr,i+1)
                curr.pop()
        ans=[]
        backtrack(n,[],1)
        return ans
        
