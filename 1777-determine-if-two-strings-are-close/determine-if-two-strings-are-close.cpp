class Solution {
public:
    bool closeStrings(string word1, string word2) {
        // 1. Swap any two existing char: abcde -> aecdb (b -> d)
        // 2. Transfrom every occurence of one existing char into another existing char
        // aacabb -> bbcbaa (change all a's to b's, b's to a's)
        
        // Operation 1 allows you to order the word at no cost
        // Operation 2 allows you to transform word with matched frequencies at no cost

        // only need to check whether we have the same number of frequency for both words
        if (word1.length() != word2.length()) return false;
        vector<int> word1_count(26, 0);
        vector<int> word2_count(26, 0);

        for (int i = 0; i < word1.length(); i++){
            word1_count[word1[i]-'a']++;
            word2_count[word2[i]-'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if ((word1_count[i] == 0) != (word2_count[i] == 0))
                return false;
        }

        sort(word1_count.begin(), word1_count.end());
        sort(word2_count.begin(), word2_count.end());

        return word1_count == word2_count;
    }
};