class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int prefix = 0;
        int suffix = accumulate(nums.begin() + 1, nums.end(), 0);

        for (int i = 0; i < nums.size(); i++){
            if (prefix == suffix){
                return i;
            }

            prefix += nums[i];
            if (i + 1 < nums.size()){
                suffix -= nums[i+1];
            } else {
                suffix = 0;
            }
        }

        return -1;
    }
};