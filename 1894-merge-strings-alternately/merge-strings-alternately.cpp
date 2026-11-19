class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        // need to keep track of w1 and w2
        int ptr1 = 0;
        int ptr2 = 0;

        string res = "";

        // looping both ptr1 and ptr2
        while (ptr1 < word1.size() && ptr2 < word2.size()){
            res += word1[ptr1];
            res += word2[ptr2];
            ptr1++, ptr2++;
            cout << ptr1 << ',' << ptr2 << endl;
            cout << res << endl;
        }

        // check either ptr1 > word1 or ptr2 word2        
        if (ptr1 == word1.size()){
            res += word2.substr(ptr2, word2.size()-ptr2+1);
        } else if (ptr2 == word2.size()){
            res += word1.substr(ptr1, word1.size()-ptr1+1);
        }

        return res;
    }
};