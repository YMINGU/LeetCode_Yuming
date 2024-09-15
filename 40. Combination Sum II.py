class Solution(object):
    def backtrack(self,candidates,target,totalIdx,path,ans):
            if target<0:
                return
            if target==0:
                ans.append(path)
                return
            for i in range(totalIdx,len(candidates)):
                if i>totalIdx and candidates[i]==candidates[i-1]:
                    continue
                self.backtrack(candidates,target-candidates[i],i+1,path+[candidates[i]],ans)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        candidates.sort()
        self.backtrack(candidates,target,0,[],ans)
        return ans
-------
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=set()
        def backtrack(curr,curr_sum,idx):
            if curr_sum==target:
                ans.add(tuple(curr))
                return
            elif curr_sum>target:
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                backtrack(curr+[candidates[i]],curr_sum+candidates[i],i+1)
        candidates.sort()
        backtrack([],0,0)
        return ans
        
