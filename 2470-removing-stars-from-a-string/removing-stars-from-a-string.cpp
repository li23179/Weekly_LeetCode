class Solution {
public:
    string removeStars(string s) {
        // "lecoe*cod*e" -> "lecoe"
        //      j    i
        // use a stack to store char, when we met it pop the top
        int j = 0;
        for (int i = 0; i < s.length(); i++){
            if (s[i] == '*'){
                j--;
            } else {
                s[j++] = s[i];
            }
        }
        
        return s.substr(0,j);
    }
};