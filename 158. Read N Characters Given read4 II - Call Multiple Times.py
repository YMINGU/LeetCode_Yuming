# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
from collections import deque
class Solution:
    def __init__(self):
        self.to_load=deque()
    def read(self, buf: List[str], n: int) -> int:
        read_count=0
        buf4=[""]*4
        while read_count<n:
            if len(self.to_load)>0:
                buf[read_count]=self.to_load.popleft()
                read_count+=1
            else:
                for i in range(read4(buf4)):
                    self.to_load.append(buf4[i])
                if len(self.to_load)==0:
                    break
        return read_count
