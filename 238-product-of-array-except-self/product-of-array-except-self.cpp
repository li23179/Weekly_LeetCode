class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // prefix product and a suffix product
        // nums = [1,2,3,4]
        // prefix = [1,1,2,6]
        // suffix = [24,12,4,1]
        int n = nums.size();

        vector<int> prefix(n, 1);
        vector<int> suffix(n, 1);
        vector<int> res(n, 1);

        for (int i = 1; i < n; i++){
            prefix[i] = nums[i-1] * prefix[i-1];
        }

        for (int i = n-2; i >= 0; i--){
            suffix[i] = nums[i+1] * suffix[i+1];
        }
        
        for (int i = 0; i < n; i++){
            res[i] = prefix[i] * suffix[i];
        }

        return res;
    }
};