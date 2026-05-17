class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> mp = new HashMap<>();

        for(int num : nums){
            mp.put(num, mp.getOrDefault(num, 0)+1);
        }

        int i = 0;
        int[] ans = new int[k];
        while(k > 0){
            int max = -1;
            int num = -1;

            for(int key : mp.keySet()){
                int freq = mp.get(key);

                if(freq > max){
                    max = freq;
                    num = key;
                }
            }

            ans[i] = num;
            mp.remove(num);
            i++;
            k--;
        }

        return ans;
    }
}
