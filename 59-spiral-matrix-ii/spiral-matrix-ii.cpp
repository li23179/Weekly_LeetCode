class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // right, down, left, up 4 operation
        // 4 border the up_border, down_border, left and right border
        // when we hit a border we want to change the direction + shrink the border
        int left = 0, right = n-1;
        int top = 0, bottom = n-1;

        vector<vector<int>> mat(n, vector<int>(n, 0));
        int i = 0, j = 0;
        int count = 1;

        while (left <= right && top <= bottom){
            for (int j = left; j <= right; j++){
                mat[top][j] = count;
                count++;
            }
            top++;

            for (int i = top; i <= bottom; i++){
                mat[i][right] = count;
                count++;
            }
            right--;

            for (int j = right; j >= left; j--){
                mat[bottom][j] = count;
                count++;
            }
            bottom--;

            for (int i = bottom; i >= top; i--){
                mat[i][left] = count;
                count++;
            }
            left++;
        }
        return mat;
    }
};