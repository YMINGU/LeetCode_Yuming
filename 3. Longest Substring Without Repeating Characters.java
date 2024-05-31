class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> chars=new HashMap();
        int left=0;
        int right=0;
        int res=0;
        while(right<s.length()){
            char r=s.charAt(right);
            chars.put(r,chars.getOrDefault(r,0)+1);
            while (chars.get(r)>1){
                char l=s.charAt(left);
                chars.put(l,chars.get(l)-1);
                left++;
            }
            res=Math.max(res,right-left+1);
            right++;
        }
        return res;
    }
}

-----------------------------------------------------
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans=0;
        Map<Character, Integer> map=new HashMap<>();
        for(int i=0,j=0;j<s.length();j++){
            if(map.containsKey(s.charAt(j))){
                i=Math.max(map.get(s.charAt(j)),i);
            }
            ans=Math.max(ans,j-i+1);
            map.put(s.charAt(j),j+1);
        }
        return ans;
    }
}



---------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic=set()
        left=right=ans=0
        while right<len(s):
            if s[right] not in dic:
                dic.add(s[right])
                right+=1
                ans=max(ans,right-left)
            else:
                dic.remove(s[left])
                left+=1
        return ans
                
            
        
