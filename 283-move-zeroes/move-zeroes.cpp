class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // left ptr keep track of the index of the zeros
        // right ptr keep track of the index of the non-zero element
        // perform a swap
        int l = 0;
        int n = nums.size();

        while (l < n){
            // locate the zero
            while (l < n && nums[l] != 0){
                l++;
            }

            int r = l + 1;
            while (r < n && nums[r] == 0){
                r++;
            }

            if (r >= n) break;
            swap(nums[l],  nums[r]);
            l++;
        }
    }
};