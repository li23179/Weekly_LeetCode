class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0;
        int maxCount = 0;
        int count = 0;

        for (int r = 0; r < nums.size(); r++){
            // update count if we met 1
            if (nums[r] == 1){
                count++;
                maxCount = max(count, maxCount);
                continue;
            }

            // if we met 0, two case: enough k and ran out of k
            // k > 0, use it and update count
            if (k > 0){
                k--;
                count++;
            } else {
                // not enough k, update l, if nums[l] == 0 then k++
                while (k == 0){
                    if (nums[l] == 0){
                        k++;
                    }
                    l++;
                    count--;
                }
                // Include the new zero
                k--;
                count++;
            }
            maxCount = max(count, maxCount);
        }

        return maxCount;
    }
};