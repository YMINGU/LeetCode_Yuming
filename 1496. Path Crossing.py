class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions={'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
        row,col=0,0
        seen={(0,0)}
        for d in path:
            dx,dy=directions[d]
            row+=dx
            col+=dy
            if (row,col) in seen:
                return True
            seen.add((row,col))
        return False
                
        
