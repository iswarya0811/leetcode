class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        set<int>s;
        int cnt=0;
        for(int i=0;i<nums.size();i++)
        {
            s.insert(nums[i]);
        }
        for(int val : s)
        {
            if(val!=0)
            {
                cnt++;
            }
        }
        return cnt;
    }
};