class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // right, down, left, up 4 operation
        // 4 border the up_border, down_border, left and right border
        // when we hit a border we want to change the direction + shrink the border
        int up_border = 0, down_border = n;
        int left_border = -1, right_border = n;
        vector<vector<int>> mat(n, vector<int>(n, 0));
        int i = 0, j = 0;
        int count = 1;
        
        while (count <= n*n){
            // move right
            while (j < right_border && count <= n*n){
                mat[i][j] = count;
                j++;
                count++; 
            }
            right_border--;
            j--;
            i++;

            // move down
            while (i < down_border && count <= n*n){
                mat[i][j] = count;
                i++;
                count++;
            }
            down_border--;
            i--;
            j--;

            // move left
            while (j > left_border && count <= n*n){
                mat[i][j] = count;
                j--;
                count++;
            }
            left_border++;
            j++;
            i--;

            // move up
            while (i > up_border && count <= n*n){
                mat[i][j] = count;
                i--;
                count++;
            }
            up_border++;
            i++;
            j++;
        }

        return mat;
    }
};