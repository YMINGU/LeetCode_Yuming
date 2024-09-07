class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans=0
        left=0
        right=len(height)-1
        while left<right:
            width=right-left
            ans=max(ans,width*min(height[left],height[right]))
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return ans
        
