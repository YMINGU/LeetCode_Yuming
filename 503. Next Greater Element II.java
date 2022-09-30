class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            res[i]=-1;
            for(int j=1;j<nums.length;j++){
                if(nums[(i+j)%nums.length]>nums[i]){
                    res[i]=nums[(i+j)%nums.length];
                    break;
                }
            }
        }
        return res;
        
    }
}

------------------------------------------------------
public class Solution {

    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 2 * nums.length - 1; i >= 0; --i) {
            while (!stack.empty() && nums[stack.peek()] <= nums[i % nums.length]) {
                stack.pop();
            }
            res[i % nums.length] = stack.empty() ? -1 : nums[stack.peek()];
            stack.push(i % nums.length);
        }
        return res;
    }
}
