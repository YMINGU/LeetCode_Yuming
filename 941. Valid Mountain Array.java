class Solution {
    public boolean validMountainArray(int[] arr) {
        boolean result=false;
        boolean p1=true;
        boolean p2=true;
        if(arr.length>=3){
            for(int i=1;i<arr.length-1;i++){
                for(int j=i;j>0;j--){
                    if(arr[j]-arr[j-1]<=0){
                        p1=false;
                        break;
                    }
                }
                for(int k=i;k<arr.length-1;k++){
                    if(arr[k]-arr[k+1]<=0){
                        p2=false;
                        break;
                    }
                }
                if(p1 && p2){
                    result=true;
                }
                else{
                    p1=true;
                    p2=true;
                }
            }
        }
        return result;
        
    }
}

-------------------------------------------------------

class Solution {
    public boolean validMountainArray(int[] arr) {
        int i=0;
        int N=arr.length;
        while(i+1<N && arr[i]<arr[i+1]){
            i++;
        }
        if(i==0 || i==N-1){
            return false;
        }
        while (i+1<N && arr[i]>arr[i+1]){
            i++;
        }
        return i==N-1;        
    }
}
