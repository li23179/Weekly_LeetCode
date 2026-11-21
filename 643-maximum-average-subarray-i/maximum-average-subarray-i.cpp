class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int l = 0, r = k;
        double maxAverage = accumulate(nums.begin(), nums.begin()+k, 0.0) / k;
        double currAverage = maxAverage;

        while (r < nums.size()){
            currAverage = currAverage * k - nums[l++];
            currAverage += nums[r++];
            currAverage /= k;
            maxAverage = max(currAverage, maxAverage);
        }

        return maxAverage;
    }
};