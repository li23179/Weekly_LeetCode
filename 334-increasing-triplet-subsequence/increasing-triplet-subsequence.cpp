class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        // brute force check every combination -> cost O(n^3)
        // we want a to be small and maintain the b > a property and index of b > index of a and if there is a number c > b then return true else 0
        int a = INT_MAX;
        int b = INT_MAX;

        for (int num : nums){
            if (num <= a) a = num;
            else if (num <= b) b = num;
            else return true;
        }

        return false;
    }
};