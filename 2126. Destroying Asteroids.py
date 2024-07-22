from heapq import *
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapify(asteroids)
        if mass<asteroids[0]:
            return False
        while len(asteroids)>0:
            asteroid=heappop(asteroids)
            if asteroid<=mass:
                mass+=asteroid
            else:
                return False
        return True

------
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid>mass:
                return False
            mass+=asteroid
        return True
        
