class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        large=[-1]*len(arr)
        small=[-1]*len(arr)
        stack=[]
        for i,x in sorted(enumerate(arr),key=lambda x:(x[1],x[0])):
            while stack and stack[-1]<i:
                large[stack.pop()]=i
            stack.append(i)
        stack=[]
        for i,x in sorted(enumerate(arr),key=lambda x:(-x[1],x[0])):
            while stack and stack[-1]<i:
                small[stack.pop()]=i
            stack.append(i)
        odd=[0]*len(arr)
        even=[0]*len(arr)
        odd[-1]=even[-1]=1
        for i in reversed(range(len(arr))):
            if 0<=large[i]:
                odd[i]=even[large[i]]
            if 0<=small[i]:
                even[i]=odd[small[i]]
        return sum(odd)
        
