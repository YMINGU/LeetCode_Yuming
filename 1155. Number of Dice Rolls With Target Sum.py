class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        @cache
        def backtrack(i, _sum):
            if i == n:
                return 1 if _sum == target else 0
            if _sum > target:
                return 0
            res = 0
            for face in range(1, k + 1):
                res += backtrack(i + 1, _sum + face)
            return res % mod

        return backtrack(0, 0)
        
