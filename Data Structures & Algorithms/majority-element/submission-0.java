class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<>();

        for(int ele: nums){
            mp.put(ele, mp.getOrDefault(ele, 0)+1);
            if(mp.get(ele) > (nums.length)/2)return ele;
        }
        return 0;
    }
}