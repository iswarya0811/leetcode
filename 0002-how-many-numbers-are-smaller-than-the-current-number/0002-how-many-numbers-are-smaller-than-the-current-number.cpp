class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>ans(nums.size());
        int n = nums.size();
        int j=0;
        for(int i=0;i<n;i++){
            int sum=0;
        for(int j=0;j<n;j++)
        {
            
            if(nums[j]<nums[i])
            {
                sum++;

            }
        }
        ans[i]=sum;
      
        }
        return ans;
    }
};