from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.count=SortedDict()
        self.max=2
    def book(self, startTime: int, endTime: int) -> bool:
        self.count[startTime]=self.count.get(startTime,0)+1
        self.count[endTime]=self.count.get(endTime,0)-1
        overlap=0
        for count in self.count.values():
            overlap+=count
            if overlap>self.max:
                self.count[startTime]-=1
                self.count[endTime]+=1
                if self.count[startTime]==0:
                    del self.count[startTime]
                return False
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
