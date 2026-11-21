class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // left ptr keep track of the index of the zeros
        // right ptr keep track of the index of the non-zero element
        // perform a swap
        int l = 0;
        int n = nums.size();

        for (int r = 0; r < n; r++){
            // locate non-zero element
            if (nums[r] == 0) continue;
            swap(nums[l], nums[r]);
            l++;
        }
    }
};