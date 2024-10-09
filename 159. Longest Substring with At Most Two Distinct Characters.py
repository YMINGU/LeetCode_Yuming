class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans=0
        l,r=0,0
        window_count={}
        while r<len(s):
            char=s[r]
            window_count[char]=window_count.get(char,0)+1
            if len(window_count)<=2:
                ans=max(ans,r-l+1)
            while len(window_count)>2:
                char=s[l]
                window_count[char]-=1
                if window_count[char]==0:
                    del window_count[char]
                l+=1
            r+=1
        return ans
---------
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n=len(s)
        if n<3:
            return n
        left,right=0,0
        hashmap=defaultdict()
        max_len=2
        while right<n:
            hashmap[s[right]]=right
            right+=1
            if len(hashmap)==3:
                del_idx=min(hashmap.values())
                del hashmap[s[del_idx]]
                left=del_idx+1
            max_len=max(max_len,right-left)
        return max_len
        
        
        
