class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // prefix product and a suffix product
        // nums = [1,2,3,4]
        // prefix = [1,1,2,6]
        // suffix = [24,12,4,1]

        // O(n) space, O(n) time complexity
        // O(1) space ? we only keep track or the previous prefix product and the suffix product
        int n = nums.size();
        vector<int> res(n, 1);

        // prefix at index 0 is always 1
        // [1,2,3,4] prefix = 2
        // [1,1,2,6]
        // [1,12,4,1]
        int prefix = 1;
        for (int i = 1; i < n; i++){
            prefix *= nums[i-1];
            res[i] *= prefix;
        }

        // suffix at the index n-1 is always 1
        int suffix = 1;
        for (int i = n-2; i >= 0; i--){
            suffix *= nums[i+1];
            res[i] *= suffix;
        }
    
        return res;
    }
};