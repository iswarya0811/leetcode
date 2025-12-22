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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>ans;
        if(root==NULL) return ans;
        queue<TreeNode*>Q;
        Q.push(root);
        while(!Q.empty()){
            int len=Q.size();
            vector<int>curr_lev;
            for(int i=0;i<len;i++)
            {
                TreeNode *node=Q.front();
                Q.pop();
                curr_lev.push_back(node->val);
                if(node->left!=NULL)
                Q.push(node->left);
                if(node->right!=NULL)
                Q.push(node->right);
            }
            ans.push_back(curr_lev);
         }
         return ans;

        
    }
};