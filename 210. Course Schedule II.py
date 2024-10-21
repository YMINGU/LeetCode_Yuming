from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        indegree={}
        for dest,src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest]=indegree.get(dest,0)+1
        zero_queue=deque([k for k in range(numCourses) if k not in indegree])
        ans=[]
        while zero_queue:
            vertex=zero_queue.popleft()
            ans.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        zero_queue.append(neighbor)
        return (ans if len(ans)==numCourses else []) 
            
        
