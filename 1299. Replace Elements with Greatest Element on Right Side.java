class Solution {
    public int[] replaceElements(int[] arr) {
        for(int i=0;i<arr.length-1;i++){
            int k = 0;
            for(int j=1;i+j<arr.length;j++){
                k = Math.max(k,arr[i+j]);
                arr[i]= k ;
            }
        }
        arr[arr.length-1]=-1;
        return arr;
        
    }
}


