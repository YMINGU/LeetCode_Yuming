class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join([str(c) for c in digits]))
        num+=1
        ans=[]
        for c in str(num):
            ans.append(int(c))
        return ans
            
------
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n):
            idx=n-1-i
            if digits[idx]==9:
                digits[idx]=0
            else:
                digits[idx]+=1
                return digits
        return [1]+digits
        
