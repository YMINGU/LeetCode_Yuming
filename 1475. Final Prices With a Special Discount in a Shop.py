
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices
------
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n=len(prices)
        res=[0]*n
        stack=[]
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack:
                res[i]=prices[i]-stack[-1]
            else:
                res[i]=prices[i]
            stack.append(prices[i])
        return res
        
