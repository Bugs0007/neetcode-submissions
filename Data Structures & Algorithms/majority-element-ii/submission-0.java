class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ans = new ArrayList<>();

        Map<Integer, Integer> mp = new HashMap<>();
        for(int ele : nums){
            mp.put(ele, mp.getOrDefault(ele, 0)+1);
        }

        for(int key : mp.keySet()){
            int freq = mp.get(key);

            if(freq > nums.length/3){
                ans.add(key);
            }
        }

        return ans;
    }
}