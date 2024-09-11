from heapq import *
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        flowers.sort()
        sorted_people=sorted(people)
        dic={}
        heap=[]
        i=0
        for person in sorted_people:
            while i<len(flowers) and flowers[i][0]<=person:
                heappush(heap,flowers[i][1])
                i+=1
            while heap and heap[0]<person:
                heappop(heap)
            dic[person]=len(heap)
        return [dic[x] for x in people]
  -----
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        starts=[]
        ends=[]
        for start,end in flowers:
            starts.append(start)
            ends.append(end+1)
        starts.sort()
        ends.sort()
        ans=[]
        for person in people:
            i=bisect.bisect_right(starts,person)
            j=bisect.bisect_right(ends,person)
            ans.append(i-j)
        return ans
        
