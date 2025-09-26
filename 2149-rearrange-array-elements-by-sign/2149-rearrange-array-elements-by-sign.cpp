class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int>res(nums.size());
        int j=1,k=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]>0)
            {
                res[k]=nums[i];
                k+=2;
            }
            else
            {
                res[j]=nums[i];
                j+=2;
            }

        }
        return res;

    }
};