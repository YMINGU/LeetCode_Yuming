from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_list=Counter(arr)
        n=len(arr)
        arr_list=sorted(arr_list.values(),reverse=True)
        ans=0
        k=0
        for key in arr_list:
            ans+=1
            k+=key
            if k>=n/2:
                break
        return ans
                    
        
        
        
