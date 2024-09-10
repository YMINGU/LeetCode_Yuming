class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        height_map=[[] for _ in range(101)]
        for l,h in rectangles:
            height_map[h].append(l)
        for heights in height_map:
            heights.sort()
        ans=[]
        for x,y in points:
            sum_angle=0
            for h in range(y,101):
                sum_angle+=len(height_map[h])-bisect.bisect_left(height_map[h],x)
            ans.append(sum_angle)
        return ans
        
