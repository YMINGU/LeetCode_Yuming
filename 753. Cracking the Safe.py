class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(node,k,seen,result):
            for i in range(k):
                edge=node+str(i)
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:],k,seen,result)
                    result.append(str(i))
        if n==1:
            return "".join(map(str,range(k)))
        seen=set()
        result=[]
        start_node="0"*(n-1)
        dfs(start_node,k,seen,result)
        return "".join(result)+start_node
