class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] left = new int[n];
        int[] right = new int[n];
        left[0] = 0;
        right[n-1] = 0;
        int max = height[0];
        for (int i = 1; i < n; i++) {
            left[i] = max;
            max = Math.max(max, height[i]);
        }
        max = height[n-1];
        for (int i = n-2; i >= 0; i--) {
            right[i] = max;
            max = Math.max(max, height[i]);
        }
        int count = 0;
        for(int i = 0; i < n; i++) {
            int val = Math.min(left[i], right[i])-height[i];
            if (val > 0) count += val;
        }
        return count;
    }
}
-----------------------------------------------------------------
class Solution {
    public int trap(int[] height) {
        if(height.length==0){
            return 0;
        }
        int ans=0;
        int n=height.length;
        int[] left=new int[n];
        int[] right=new int[n];
        left[0]=height[0];
        for(int i=1;i<n;i++){
            left[i]=Math.max(height[i],left[i-1]);
        }
        right[n-1]=height[n-1];
        for(int i=n-2;i>=0;i--){
            right[i]=Math.max(height[i],right[i+1]);
        }
        for(int i=1;i<n;i++){
            ans+=Math.min(left[i],right[i])-height[i];
        }
        return ans;
    }
}
-------------------------------------------------------------------
class Solution {
    public int trap(int[] height) {
        int n=height.length;
        int i=0;
        int j=n-1;
        int left=0;
        int right=0;
        int ans=0;
        while(i<j){
            if(height[i]<height[j]){
                if(left>height[i]){
                    ans+=left-height[i];
                }
                else{
                    left=height[i];
                }
                i++;
            }
            else{
                if(right>height[j]){
                    ans+=right-height[j];
                }
                else{
                    right=height[j];
                }
                j--;
            }
            
        }
        return ans;
    }
}
