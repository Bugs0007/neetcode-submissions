class Solution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void quickSort(int[] arr, int low, int high){
        if(low >= high) return;

        int pivot = arr[high]; // simple pivot
        int i = low;

        for(int j = low; j < high; j++){
            if(arr[j] < pivot){
                swap(arr, i, j);
                i++;
            }
        }

        swap(arr, i, high);

        quickSort(arr, low, i - 1);
        quickSort(arr, i + 1, high);
    }

    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}