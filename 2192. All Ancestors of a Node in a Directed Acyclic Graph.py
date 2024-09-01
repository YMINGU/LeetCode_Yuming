class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[[] for _ in range(n)]
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
        for i in range(n):
            self.dfs(i,adj,i,ans)
        return ans
    def dfs(self,ancestor,adj,curr,ans):
        for child in adj[curr]:
            if not ans[child] or ans[child][-1]!=ancestor:
                ans[child].append(ancestor)
                self.dfs(ancestor,adj,child,ans)
