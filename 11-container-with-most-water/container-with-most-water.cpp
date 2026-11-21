class Solution {
public:
    int maxArea(vector<int>& height) {
        // area = min(l, r) * (r - l)
        int l = 0, r = height.size() - 1;
        int maxArea = INT_MIN;
        while (l < r){
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l));
            if (height[l] > height[r]){
                r--;
            } else {
                l++;
            }
        }
        return maxArea;
    }
};