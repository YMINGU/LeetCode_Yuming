class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        N=len(num1)+len(num2)
        answer=[0]*N
        first=num1[::-1]
        second=num2[::-1]
        for p2,d2 in enumerate(second):
            for p1,d1 in enumerate(first):
                num_zeros=p1+p2
                carry=answer[num_zeros]
                multi=int(d1)*int(d2)+carry
                answer[num_zeros]=multi%10
                answer[num_zeros+1]+=multi//10
        if answer[-1]==0:
            answer.pop()
        return "".join(str(digit) for digit in reversed(answer))
        
