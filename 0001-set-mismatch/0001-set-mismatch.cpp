class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int totsum = (nums.size()*(nums.size()+1))/2;
        int dup,sum=0;
        for(int i=0;i<nums.size()-1;i++)
        {
            if(nums[i]==nums[i+1])
            {
                dup=nums[i];
                
            }
            sum+=nums[i];
        }
        sum+=nums[nums.size()-1];
        vector<int>ans;
        int missing = totsum-(sum-dup);
        ans.push_back(dup);
        ans.push_back(missing);
        return ans;
    }
};