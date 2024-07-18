class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        q=[start]
        while q:
            node=q.pop()
            if arr[node]==0:
                return True
            if arr[node]<0:
                continue
            for i in [node+arr[node],node-arr[node]]:
                if 0<=i<n:
                    q.append(i)
            arr[node]=-arr[node]
        return False
    -------
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0<=start<len(arr) and arr[start]>=0:
            if arr[start]==0:
                return True
            arr[start]=-arr[start]
            return self.canReach(arr,start+arr[start]) or self.canReach(arr,start-arr[start])
        return False
        
