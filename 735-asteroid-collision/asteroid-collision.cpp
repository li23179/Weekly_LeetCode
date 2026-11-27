class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        // use a stack to store the current asteriod, 
        // stack only allows the same direction
        // if we met an asteriod that is in different direction at the top of the stack
        // compare(top, a) if abs(a) > abs(top) pop the top, then compare to the next top
        // until either abs(a) == abs(top) (both explode) or abs(a) < abs(top) then stop
        vector<int> st;

        for (int a : asteroids){
            bool alive = true;

            while (alive && a < 0 && !st.empty() && st.back() > 0){
                if (st.back() < -a){
                    st.pop_back();
                } else if (st.back() == -a) {
                    st.pop_back();
                    alive = false;
                } else {
                    alive = false;
                }
            }

            if (alive) st.push_back(a);
        }

        return st;
    }
};