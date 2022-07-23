class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int arr[]=new int [26];
        for (int i=0;i<magazine.length();i++){
            arr[magazine.charAt(i)-'a']++;
        }
        for (int j=0;j<ransomNote.length();j++){
            if(arr[ransomNote.charAt(j)-'a']-1<0){
                return false;
            }
            arr[ransomNote.charAt(j)-'a']--;
        }
        return true;
        
    }
}
