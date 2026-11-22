class Solution {
public:
    bool checkString(string s) {
        bool encounterB = false;
        for (int i = 0; i < s.size(); i++){
            if (encounterB && s[i] == 'a') return false;
            if (s[i] == 'b') encounterB = true;
        }
        return true;
    }
};