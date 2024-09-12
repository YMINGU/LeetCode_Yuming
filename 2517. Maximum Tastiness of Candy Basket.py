class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        def pick(mid):
            count=1
            lpick=price[0]
            for i in range(1,len(price)):
                if price[i]-lpick>=mid:
                    lpick=price[i]
                    count+=1
                    if count>=k:
                        return True
            return False
        left=0
        right=price[-1]-price[0]
        while left<=right:
            mid=(left+right)//2
            if pick(mid):
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans
        
