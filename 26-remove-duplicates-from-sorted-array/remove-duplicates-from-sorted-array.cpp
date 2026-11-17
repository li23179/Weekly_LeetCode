class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // one variable keep track of which pos do i need to place the num
        // one variable keep track of the first encounter num
        int k = 1;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] == nums[i-1]){
                continue;
            }

            nums[k] = nums[i];
            k++;
        }

        return k;
    }
};