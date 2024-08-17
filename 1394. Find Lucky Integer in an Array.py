from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count=Counter(arr)
        ans=[]
        for key in count.keys():
            if count[key]==key:
                ans.append(key)
        return max(ans) if ans else -1
        
  ---
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        curr=0
        for i in range(len(arr)):
            curr+=1
            if i==len(arr)-1 or arr[i]!=arr[i+1]:
                if arr[i]==curr:
                    return arr[i]
                curr=0
        return -1
        
