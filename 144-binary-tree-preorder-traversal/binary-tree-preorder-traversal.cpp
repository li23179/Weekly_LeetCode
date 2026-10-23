/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        // push the root node first -> then push right and left onto the stack
        if (!root) return {};
        
        stack<TreeNode*> st;
        vector<int> res;
        st.push(root);

        while (!st.empty()){
            // pop the top then push right and left
            TreeNode* node = st.top();
            st.pop();

            if (node->right){
                st.push(node->right);
            }
            
            if (node->left){
                st.push(node->left);
            }

            res.push_back(node->val);
        }

        return res;
    }
};