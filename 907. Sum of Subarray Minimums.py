class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD=10**9+7
        stack=[]
        sum_min=0
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]]>=arr[i]):
                mid=stack.pop()
                left=-1 if not stack else stack[-1]
                right=i
                count=(mid-left)*(right-mid)
                sum_min+=(count*arr[mid])
            stack.append(i)
        return sum_min%MOD
            
        
