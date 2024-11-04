class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen=set()
        ans=float("inf")
        for x1,y1 in points:
            for x2,y2 in points:
                if (x1,y2) in seen and (x2,y1) in seen:
                    ans=min(ans,abs((x2-x1)*(y2-y1)))
            seen.add((x1,y1))
        return ans if ans!=float("inf") else 0
        
