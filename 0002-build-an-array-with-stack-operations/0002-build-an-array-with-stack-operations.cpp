class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
       
       vector<string>ans;
       int j=0;
       for(int i=1;i<=n && j < target.size();i++)
       {
            
            auto found = find(target.begin(),target.end(),i);
            if(found==target.end()){
            ans.push_back("Push");
            ans.push_back("Pop");
            }
            else{   
                ans.push_back("Push");
                j++;
            }
            
       } 
       return ans;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna