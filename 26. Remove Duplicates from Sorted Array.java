class Solution {
    public int removeDuplicates(int[] nums) {
        int i=1;
        for (int j=1;j<=nums.length-1;j++){
            if(nums[j]!=nums[j-1]){
                nums[i]=nums[j];
                i++;
            }

        }
        return i;
        
    }
}

--------------------------------------------------
class Solution {
    public int removeDuplicates(int[] nums) {
        int count=1;
        int i=0;      
        for (int j=1;j<nums.length;j++){
            if(nums[j]!=nums[i]){
                count++;
                nums[++i]=nums[j];

            }

        }
        return count;      
    }
}  
