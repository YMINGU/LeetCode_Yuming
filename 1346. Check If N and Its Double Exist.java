class Solution {
    public boolean checkIfExist(int[] arr) {
        boolean result=false;
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                if(i!=j){
                if(arr[i]==2*arr[j]){
                    result=true;
                    break;
                }
                }
            }
            
        }
        return result;
        
    }
}
