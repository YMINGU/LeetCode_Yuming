class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j = n-1;
        int i = m-1;
        while(i+j+1>=0) {
        	if(j==-1) {
        		break;
        	}
        	else if (i==-1) {
        		nums1[j+i+1] = nums2[j];
        		j--;
        	}
        	else {
        		int n1=nums1[i], n2=nums2[j];
        		int num = Math.max(n1, n2);
        		nums1[j+i+1] = num;
        		if(n1==num) i--;
        		else j--;
        	}
        }
    }
}

----------------------------------------------------------------
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i=m;i<nums1.length;i++){
            nums1[i]=nums2[i-m];
        }
        Arrays.sort(nums1);
            
        }
        
    }
