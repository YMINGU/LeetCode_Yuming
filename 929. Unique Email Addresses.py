class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans=[]
        for email in emails:
            local=email.split("@")[0]
            domain=email.split("@")[1]
            local=local.split("+")[0]
            local="".join(local.split("."))
            ans.append(local+"_"+domain)
        ans_set=set(ans)
        return len(ans_set)
            
      -----
