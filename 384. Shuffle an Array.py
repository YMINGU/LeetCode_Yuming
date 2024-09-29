import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.copy=nums.copy()
        
        

    def reset(self) -> List[int]:
        return self.copy
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
------
class Solution:

    def __init__(self, nums: List[int]):
        self.array=nums
        self.original=list(nums)
        

    def reset(self) -> List[int]:
        self.array=self.original
        self.original=list(self.original)
        return self.array
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            idx=random.randrange(i,len(self.array))
            self.array[i],self.array[idx]=self.array[idx],self.array[i]
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
