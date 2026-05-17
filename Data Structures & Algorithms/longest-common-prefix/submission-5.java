class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int len = strs.length;
        int n = Math.min(strs[0].length(), strs[len-1].length());
        int i=0;
        String ans = "";

        while(i < n){
            if(strs[0].charAt(i) != strs[len-1].charAt(i)){
                break;
            }
            i++;
        }

        return strs[0].substring(0, i);
    }
}