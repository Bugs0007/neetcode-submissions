class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int num = nums[i];
            int req = target - num;

            if(mp.containsKey(req)){
                return new int[]{mp.get(req), i};
            }else{
                mp.put(num, i);
            }
        }

        return new int[2];
    }
}
