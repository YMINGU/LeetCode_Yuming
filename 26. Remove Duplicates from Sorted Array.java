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

---------------------------------------------------
class Solution {
    public int removeDuplicates(int[] nums) {
        int count=0;
        for(int i=nums.length-1;i>0;i--){
            if(nums[i]==nums[i-1]){
                for(int j=i;j+1<nums.length;j++){
                    nums[j]=nums[j+1];
                }
                count++;
            }
        }
        return nums.length-count;        
    }
}
