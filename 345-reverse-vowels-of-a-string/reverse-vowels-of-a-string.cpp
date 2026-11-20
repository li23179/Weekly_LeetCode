class Solution {
public:
    string reverseVowels(string s) {
        // two pointer to track the vowel at the back
        // and at the front
        int l = 0, r = s.size()-1;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'}; 
        while (l < r){
            while (l < r && !vowels.count(tolower(s[l]))){
                l++;
            }

            while (l < r && !vowels.count(tolower(s[r]))){
                r--;
            }
            
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;

            l++, r--;
        }

        return s;
    }
};