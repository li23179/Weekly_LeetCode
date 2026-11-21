class Solution {
public:
    bool isSubsequence(string s, string t) {
        // Need to loop through each s char
        // if we finished t but not finish s then s is not a subsequence
        int i = 0;
        int j = 0;

        while (i < s.size() && j < t.size()){
            if (s[i] == t[j]){
                i++;
            }
            j++;
        }

        return i == s.size();
    }
};