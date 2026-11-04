class Solution {
public:
    vector<int> grayCode(int n) {
        // invlusive range (0, 2^n-1)
        // first integer 0
        // integer appears no more than once in the sequence
        // binary representation of every pair adjacent integers differs by one bit
        // first and last integers differs exactly one bit
        vector<int> res;

        for (int i = 0; i < 1 << n; i++){
            res.push_back(i ^ (i >> 1));
        }

        return res;

    }
};