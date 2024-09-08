class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        init = n
        x = 1
        while self.get_sum(n) > target:
            n = ((n // (10**x)) + 1) * (10**x)
            x += 1
        return n - init

    def get_sum(self, n):
        return sum([int(d) for d in str(n)])
        
        
