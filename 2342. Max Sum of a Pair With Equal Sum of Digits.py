from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum=0
            while num:
                digit_sum+=num%10
                num//=10
            return digit_sum
        dic=defaultdict(int)
        ans=-1
        for num in nums:
            digit_sum=get_digit_sum(num)
            if digit_sum in dic:
                ans=max(ans,num+dic[digit_sum])
            dic[digit_sum]=max(dic[digit_sum],num)
        return ans
            
            
        
