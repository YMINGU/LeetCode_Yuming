class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*(max(trip[2] for trip in trips)+1)
        for (value,left,right) in trips:
            arr[left]+=value
            arr[right]-=value
        curr=0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr>capacity:
                return False
        return True
        
