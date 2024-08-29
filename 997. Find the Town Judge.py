class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)<n-1:
            return -1
        indegree=[0]*(n+1)
        outdegree=[0]*(n+1)
        for a,b in trust:
            outdegree[a]+=1
            indegree[b]+=1
        for i in range(1,n+1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1

-----
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)<n-1:
            return -1
        scores=[0]*(n+1)
        for a,b in trust:
            scores[a]-=1
            scores[b]+=1
        for i,score in enumerate(scores[1:],1):
            if score==n-1:
                return i
        return -1
        
