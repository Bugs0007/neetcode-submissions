class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mp = new HashMap<>();

        for(String str: strs){
            char[] s = str.toCharArray();
            Arrays.sort(s);
            String sorted = new String(s);

            if(mp.containsKey(sorted)){
                mp.get(sorted).add(str);
            }else{
                mp.put(sorted, new ArrayList<>());
                mp.get(sorted).add(str);
            }
        }

        return new ArrayList<>(mp.values());
    }
}
