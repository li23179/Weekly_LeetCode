class Solution {
public:
    string reverseWords(string s) {
        // trim the white space first, skip the
        // skip the leading and trailing spaces
        
        // perform a word search each time, skip multiple spaces
        int l = 0;
        for (int r = 0; r < s.size(); r++){
            if (s[r] == ' ') continue;

            // no need to insert a space when it is the first word
            // insert a space char when we met a new word
            if (l > 0){
                s[l] = ' ';
                l++;
            }

            // fill in the char in left to push the char the front
            while (r < s.size() && s[r] != ' '){
                s[l] = s[r];
                l++, r++;
            }
        }

        // resize it to l pointer
        s.resize(l);

        // reverse the whole word
        reverse(s.begin(), s.end());

        // reverse each word
        int start = 0;
        // "the sky is blue"
        for (int i = 0; i <= s.size(); i++){
            if (i == s.size() || s[i] == ' '){
                reverse(s.begin()+start, s.begin()+i);
                start = i+1;
            }
        }
        
        return s;
    }
};