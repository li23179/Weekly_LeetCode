class Solution {
private:
    bool isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' ||
               c == 'o' || c == 'u';
    }


public:
    int maxVowels(string s, int k) {
        int maxVowel = 0;
        for (int i = 0; i < k; i++){
            if (isVowel(s[i])) maxVowel++;
        }

        int count = maxVowel;
        int l = 0, r = k;
        
        while (r < s.size()){
            if (isVowel(s[l])) count--;
            if (isVowel(s[r])) count++;
            maxVowel = max(maxVowel, count);
            l++;
            r++;
        } 
        
        return maxVowel;
    }   
};