class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        // Objective: return number of pairs (r, c) st row r and c are equal
        // Use one row set and one col set, count the number of pairs that exists in two set
        map<vector<int>, int> mp;
        int n = grid.size();

        for (int i = 0; i < n; i++){
            mp[grid[i]]++;
        }
        
        int count = 0;
        for (int i = 0; i < n; i++){
            vector<int> col(n, 0);
            for (int j = 0; j < n; j++){
                col[j] = grid[j][i];
            }

            count += mp[col];
        }

        return count;
    }
};