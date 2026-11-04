#include <sstream>

class Solution {
public:
    string simplifyPath(string path) {
        // Rules must start with /
        // directories must be separated by exactly one slash
        // path must not end with a slash, unless root
        // must not have any '.', ".."
        stringstream ss(path);
        
        vector<string> segments;
        string segment;
        while(getline(ss, segment, '/')){
            if (segment.empty() || segment == "."){
                continue;
            }
            if (segment == ".."){
                if (!segments.empty()){
                    segments.pop_back();
                }
                continue;
            }
            segments.push_back(segment);
        }

        string res = "/";
        for (string seg : segments){
            res += seg + "/";
        }

        if (res != "/"){
            res.pop_back();
        }
        return res;

    }
};