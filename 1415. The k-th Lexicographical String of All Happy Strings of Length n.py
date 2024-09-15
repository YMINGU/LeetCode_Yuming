class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def backtrack(curr):
            if len(curr)==n:
                ans.append(curr[:])
                return
            for i in range(3):
                if not curr or curr[-1]!=alpha[i]:
                    curr.append(alpha[i])
                    backtrack(curr)
                    curr.pop()
        ans=[]
        alpha=['a','b','c']
        backtrack([])
        res=[]
        for i in ans:
            res.append("".join(i))
        res.sort()
        return res[k-1] if k<=len(res) else ""
