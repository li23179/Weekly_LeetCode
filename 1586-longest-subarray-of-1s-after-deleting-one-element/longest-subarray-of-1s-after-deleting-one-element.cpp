class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        // if our window contain more than one zero then shift l
        int l = 0;
        int zeros = 0;
        int longest = 0;

        int n = nums.size();
        
        for (int r = 0; r < n; r++){
            if (nums[r] == 0) zeros++;

            while (zeros > 1){
                if (nums[l] == 0) zeros--;
                l++;
            }

            longest = max(longest, r - l);
        }

        return longest;
    }
};