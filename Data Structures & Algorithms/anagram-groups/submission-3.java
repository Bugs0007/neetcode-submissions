class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mp = new HashMap<>();

        for(String word : strs){
            char[] ch = word.toCharArray();
            Arrays.sort(ch);
            String s = new String(ch);

            mp.putIfAbsent(s, new ArrayList<>());
            mp.get(s).add(word);
        }

        return new ArrayList<>(mp.values());
    }
}
