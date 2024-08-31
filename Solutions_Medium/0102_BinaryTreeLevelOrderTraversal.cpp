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
    vector<vector<int>> levelOrder(TreeNode *root) {
        if (root == nullptr) {
            return {};
        }

        vector<TreeNode *> roots_on_level = {root};
        vector<vector<int>> levels;

        while (!roots_on_level.empty()) {
            vector<int> level;
            vector<TreeNode *> new_roots;

            for (TreeNode *root : roots_on_level) {
                level.push_back(root->val);

                if (root->left != nullptr) {
                    new_roots.push_back(root->left);
                }

                if (root->right != nullptr) {
                    new_roots.push_back(root->right);
                }
            }

            levels.push_back(level);
            roots_on_level = new_roots;
        }

        return levels;
    }
};