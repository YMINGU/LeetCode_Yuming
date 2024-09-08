class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        ans=0
        while maxDoubles and target!=1:
            if target%2:
                target-=1
                ans+=1
            target/=2
            maxDoubles-=1
            ans+=1
        if target>1:
            ans+=target-1
        return ans
            
            
  -------
class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        ans=0
        while target>1 and maxDoubles:
            if target%2:
                target-=1
                ans+=1
            target/=2
            maxDoubles-=1
            ans+=1
        return ans+target-1
        
