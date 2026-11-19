class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // str1 = "ABABAB", str2 = "ABAB"
        string s;
        string t;

        if (str1.size() > str2.size()){
            s = str1;
            t = str2;
        } else {
            s = str2;
            t = str1;
        }

        string res;        
        for (int i = t.size()-1; i >= 0; i--){
            if (s.size() % (i+1) != 0 || t.size() % (i+1) != 0){
                continue;
            }
            res = t.substr(0, i+1);
            int same = true;
            for (int j = 0; j < s.size(); j++){
                if (s[j] != res[j%(i+1)] || t[j%t.size()] != res[j%(i+1)]){
                    same = false;
                    break;
                }
            }

            if (same) return t.substr(0, i+1);
        }

        return "";
    }
};