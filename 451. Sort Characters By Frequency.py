from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        ans=[]
        for letter,freq in count.most_common():
            ans.append(letter*freq)
        return "".join(ans)
      --
