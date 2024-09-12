class Solution(object):
    def get_num(self,bloomDay,mid,k):
        num_bouquets=0
        count=0
        for day in bloomDay:
            if day<=mid:
                count+=1
            else:
                count=0
            if count==k:
                num_bouquets+=1
                count=0
        return num_bouquets
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k>len(bloomDay):
            return -1
        start=0
        end=max(bloomDay)
        ans=-1
        while start<=end:
            mid=(start+end)//2
            if self.get_num(bloomDay,mid,k)>=m:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans

        
