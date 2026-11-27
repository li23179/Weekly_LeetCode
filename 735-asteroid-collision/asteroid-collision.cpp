class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        // use a stack to store the current asteriod, 
        // stack only allows the same direction
        // if we met an asteriod that is in different direction at the top of the stack
        // compare(top, a) if abs(a) > abs(top) pop the top, then compare to the next top
        // until either abs(a) == abs(top) (both explode) or abs(a) < abs(top) then stop
        stack<int> st;

        for (int i = 0; i < asteroids.size(); i++){
            // pop when one is top is right and asteriod is left
            while (!st.empty() && st.top() > 0 && asteroids[i] < 0 && abs(asteroids[i]) > abs(st.top())){
                st.pop();
            }

            // if the stack is empty then push
            if (st.empty()){
                st.push(asteroids[i]);
                continue;
            }

            // check whether the stack is not empty and the one left is == asteriods[i]
            if (st.top() > 0 && asteroids[i] < 0 && abs(asteroids[i]) == abs(st.top())){
                st.pop();
                continue;
            }

            if (st.top() > 0 && asteroids[i] < 0) continue;
            st.push(asteroids[i]);
            cout << st.top() << endl;
        } 

        vector<int> res;
        while (!st.empty()){
            res.push_back(st.top());
            st.pop();
        }

        reverse(res.begin(), res.end());
        return res;
    }
};