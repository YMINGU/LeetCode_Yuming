class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> setNums=new HashSet<>();
        for(int num:nums){
            setNums.add(num);
        }
        int maximum=Collections.max(setNums);
        if(setNums.size()<3){
            return maximum;
        }
        setNums.remove(maximum);
        int secondMaximum=Collections.max(setNums);
        setNums.remove(secondMaximum);
        return Collections.max(setNums);
        
    }
}
