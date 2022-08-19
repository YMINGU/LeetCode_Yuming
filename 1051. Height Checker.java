class Solution {
    public int heightChecker(int[] heights) {
        int count=0;
        int [] expected=new int[heights.length];
        for(int j=0;j<heights.length;j++){
            expected[j]=heights[j];
        }
        Arrays.sort(expected);
        for(int i=0;i<heights.length;i++){
            if(heights[i]!=expected[i]){
                count++;
            }
        }
        return count;
        
    }
}
