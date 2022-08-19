class Solution {
    public void moveZeroes(int[] nums) {
        int j=0;
        int k=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                k=nums[j];
                nums[j]=nums[i];
                nums[i]=k;
                j++;
                
            }
        }
    }
}
