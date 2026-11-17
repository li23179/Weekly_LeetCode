class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // we can place the nums[i] == val to the at the end of the vec
        // [2,2,3,3] 
        //     r  
        int l = 0, r = nums.size() - 1;
        while (l <= r){
            // skip all the value that is not equal to value
            while (l <= r && nums[l] != val){
                l++;
            }
            
            // skip all the value that is already value
            while (l <= r && nums[r] == val){
                r--;
            }

            if (l < r){
                int tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;

                l++;
                r--;
            }
        }
        return l;
    }
};