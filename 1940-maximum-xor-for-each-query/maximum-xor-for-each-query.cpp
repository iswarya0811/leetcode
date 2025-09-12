class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        vector<int>res(nums.size());
        int ans=pow(2,maximumBit)-1;
        int a=0,b=nums.size()-1;
        for(int i=0;i<nums.size();i++){
           a^=nums[i];
           res[b]=a^ans;
           b--;
        }
       
        return res;
    }
};