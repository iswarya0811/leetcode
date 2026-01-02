class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        map<int,int>mp;
        int ans;
        for(auto it:nums){
            mp[it]++;
        }
        int n=nums.size()/2;
        for(auto &it:mp){
            if(it.second==n)
            {
                ans=it.first;
                break;
            }
           
        }
         return ans;
    }
};