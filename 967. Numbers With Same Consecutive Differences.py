class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, i):
            if len(curr)== n:
                ans.add(int("".join(curr)))
                return 
            if i+k <10:
                curr.append(str(i+k))
                backtrack(curr,i+k)
                curr.pop()
            if i-k >-1:
                curr.append(str(i-k))
                backtrack(curr,i-k)
                curr.pop()
            
        ans =set()
        for h in range(1,10):
            backtrack([str(h)],h)
        return ans
        -----
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n==1:
            return [i for i in range(10)]
        ans=[]
        def dfs(n,num):
            if n==0:
                return ans.append(num)
            digit=num%10
            next_digits=set([digit+k,digit-k])
            for next_digit in next_digits:
                if 0<=next_digit<10:
                    new_num=num*10+next_digit
                    dfs(n-1,new_num)
        for num in range(1,10):
            dfs(n-1,num)
        return list(ans)
        ----
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n==1:
            return [i for i in range(10)]
        queue=[digit for digit in range(1,10)]
        for level in range(n-1):
            next_queue=[]
            for num in queue:
                digit=num%10
                next_digits=set([digit+k,digit-k])
                for next_digit in next_digits:
                    if 0<=next_digit<10:
                        new_num=num*10+next_digit
                        next_queue.append(new_num)
            queue=next_queue
        return queue
