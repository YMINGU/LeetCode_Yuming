class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        ans=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i]-min_price>ans:
                ans=prices[i]-min_price
        return ans
  -----
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        ans=0
        for i in range(len(prices)):
            min_price=min(min_price,prices[i])
            ans=max(ans,prices[i]-min_price)
        return ans
-----
