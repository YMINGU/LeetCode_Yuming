class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left=min(sweetness)
        right=sum(sweetness)//(k+1)
        while left<=right:
            mid=(left+right)//2
            curr=0
            piece=0
            for s in sweetness:
                curr+=s
                if curr>=mid:
                    piece+=1
                    curr=0
            if piece>=k+1:
                left=mid+1
            else:
                right=mid-1
        return right
        
