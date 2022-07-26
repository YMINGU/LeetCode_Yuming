class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for(int num:nums){
            if((num>9 && num<100) || (num>999 && num<10000) ||(num>99999 && num<1000000)){
                count++;
            }
        }
        return count;
        
    }
}
