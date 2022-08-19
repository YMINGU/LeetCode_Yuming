class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int temp=0;
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0){
                temp=nums[j];
                nums[j]=nums[i];
                nums[i]=temp;
                j++;
            }
        }
        return nums;
        
    }
}
