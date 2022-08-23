class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int left=0;
        int zeros=0;
        int count=0;
        for(int right=0;right<nums.length;right++){
            if(nums[right]==0){
                zeros++;
            }
            while(zeros==2){
                if(nums[left]==0){
                    zeros--;
                }
                left++;
            }
            count=Math.max(count,right-left+1);
        }
        return count;
    }
        
}
