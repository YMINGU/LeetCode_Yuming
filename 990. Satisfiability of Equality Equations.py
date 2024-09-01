class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph=[[] for _ in range(26)]
        for equation in equations:
            if equation[1]=='=':
                x=ord(equation[0])-ord('a')
                y=ord(equation[3])-ord('a')
                graph[x].append(y)
                graph[y].append(x)
        color=[-1]*26
        def dfs(node,c):
            if color[node]==-1:
                color[node]=c
                for nei in graph[node]:
                    dfs(nei,c)
        for i in range(26):
            if color[i]==-1:
                dfs(i,i)
        for equation in equations:
            if equation[1]=='!':
                x=ord(equation[0])-ord('a')
                y=ord(equation[3])-ord('a')
                if color[x]==color[y]:
                    return False
        return True
                
        
