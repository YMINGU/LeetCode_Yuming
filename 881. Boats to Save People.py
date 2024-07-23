class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        ans=0
        while people:
            small=people[0]
            large=people[-1]
            if small+large<=limit and len(people)>1:
                people.pop()
                people.pop(0)
            else:
                people.pop()
            ans+=1
        return ans
------
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans=0
        i=0
        j=len(people)-1
        people.sort()
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            ans+=1
        return ans
        
