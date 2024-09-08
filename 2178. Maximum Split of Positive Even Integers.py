class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum%2!=0:
            return []
        i=2
        ans=[]
        while finalSum-i>i:
            finalSum-=i
            ans.append(i)
            i+=2
        ans.append(finalSum)
        return ans
            
                
        
