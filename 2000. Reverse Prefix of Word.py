class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result=list(word)
        left=0
        for right in range(len(word)):
            if result[right]==ch:
                while left<=right:
                    result[right],result[left]=result[left],result[right]
                    left+=1
                    right-=1
                return "".join(result)
        return word
        
