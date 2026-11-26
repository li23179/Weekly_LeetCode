class Solution {
public:
    string removeStars(string s) {
        // "leet**cod*e" -> "lecoe"
        // use a stack to store char, when we met it pop the top
        stack<char> st;

        for (int i = 0; i < s.length(); i++){
            if (s[i] != '*'){
                st.push(s[i]);
            } else {
                st.pop();
            }
        }

        string res = "";
        
        while(!st.empty()){
            res += st.top();
            st.pop();
        }

        reverse(res.begin(), res.end());
        return res;
    }
};