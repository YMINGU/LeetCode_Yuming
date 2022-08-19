class Solution {
    public int removeElement(int[] nums, int val) {
        int k=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==val){
                nums[i]=99999;
                k++;
            }
        }
        Arrays.sort(nums);
        
        return nums.length-k;
        
    }
}

---------------------------------------------------------
  public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}

----------------------------------------------------------
    class Solution {
    public int removeElement(int[] nums, int val) {
        int temp=0;
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val){
                temp=nums[j];
                nums[j]=nums[i];
                nums[i]=temp;
                j++;
            }
        }
        return j;
        
    }
}
