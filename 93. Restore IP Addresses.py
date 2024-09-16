class Solution(object):
    def valid(self,s,start,length):
        return length==1 or (s[start]!="0" and (length<3 or s[start:start+length]<="255"))
    def helper(self,s,startIndex,dots,ans):
        remain_length=len(s)-startIndex
        remain_integer=4-len(dots)
        if (remain_length>remain_integer*3 or remain_length<remain_integer):
            return
        if len(dots)==3:
            if self.valid(s,startIndex,remain_length):
                temp=""
                last=0
                for dot in dots:
                    temp+=s[last:last+dot]+"."
                    last+=dot
                temp+=s[startIndex:]
                ans.append(temp)
            return
        for curPos in range(1,min(4,remain_length+1)):
            dots.append(curPos)
            if self.valid(s,startIndex,curPos):
                self.helper(s,startIndex+curPos,dots,ans)
            dots.pop()
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer=[]
        self.helper(s,0,[],answer)
        return answer
        
