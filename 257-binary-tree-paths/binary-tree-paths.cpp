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
    void dfs(TreeNode* node, string path, vector<string> &res){
        // Base case: if we hit the nullptr -> return the string
        if (!node){
            return;
        }

        // add the current node to the path
        path += to_string(node->val);

        if (!node->left && !node->right){
            res.push_back(path);
            return;
        }

        path += "->";

        dfs(node->left, path, res);
        dfs(node->right, path, res);
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        dfs(root, "", res);
        return res;
    }
};