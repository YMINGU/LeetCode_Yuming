from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        jewels_set=set(jewels)
        stone_map=defaultdict(int)
        for stone in stones:
            stone_map[stone]+=1
        for key in stone_map:
            if key in jewels_set:
                ans+=stone_map[key]
        return ans
  --------------------------------------
class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> Jset = new HashSet();
        for (char j: J.toCharArray())
            Jset.add(j);

        int ans = 0;
        for (char s: S.toCharArray())
            if (Jset.contains(s))
                ans++;
        return ans;
    }
}
