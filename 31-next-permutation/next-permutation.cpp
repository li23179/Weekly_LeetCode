class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // first the pivot
        int k = nums.size() - 2;
        while (k >= 0 && nums[k] >= nums[k+1]){
            k--;
        }

        // Step 2: Find next larger element
        if (k >= 0) {
            int j = nums.size() - 1;

            while (nums[j] <= nums[k]) {
                j--;
            }

            swap(nums[k], nums[j]);
        }

        // reverse the suffix
        reverse(nums.begin() + k + 1, nums.end());
    }
};