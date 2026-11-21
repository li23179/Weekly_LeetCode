class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int l = 0;
        int r = 0;

        while (r < n){
            char group_char = chars[r];
            int start = r;

            // skip all the chars[r] that is the same as the start char
            while (r < n && group_char == chars[r]){
                r++;
            }

            int groupLength = r - start;
            chars[l++] = group_char;

            if (groupLength > 1){
                string count = to_string(groupLength);
                for (char c : count){
                    chars[l++] = c;
                }
            }
        }

        return l;

    }
};