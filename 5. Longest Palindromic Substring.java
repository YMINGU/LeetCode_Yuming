class Solution {
    public String longestPalindrome(String s) {
        for(int length=s.length();length>0;length--){
            for(int start=0;start<=s.length()-length;start++){
                if(check(start,start+length,s)){
                    return s.substring(start,start+length);
                }
            }
        }
        return "";     
    }
    
    private boolean check(int i, int j, String s){
        int left=i;
        int right=j-1;
        while(left<right){
            if(s.charAt(left)!=s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}

------
class Solution {
    public String longestPalindrome(String s) {
        int n=s.length();
        boolean[][] dp=new boolean[n][n];
        int[] ans=new int[]{0,0};
        
        for(int i=0;i<n;i++){
            dp[i][i]=true;
        }
        for(int i=0;i<n-1;i++){
            if(s.charAt(i)==s.charAt(i+1)){
                dp[i][i+1]=true;
                ans[0]=i;
                ans[1]=i+1;
            }
        }
        
        for(int diff=2;diff<n;diff++){
            for(int i=0;i<n-diff;i++){
                int j=i+diff;
                if(s.charAt(i)==s.charAt(j) && dp[i+1][j-1]){
                    dp[i][j]=true;
                    ans[0]=i;
                    ans[1]=j;
                }
            }
        }
        int i=ans[0];
        int j=ans[1];
        return s.substring(i,j+1);     
    }
}
