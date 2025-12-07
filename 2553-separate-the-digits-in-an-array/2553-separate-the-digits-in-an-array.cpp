class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        deque<int>dq;
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(nums[i]>9)
            {
                while(nums[i]>9){
                dq.push_front(nums[i]%10);
                nums[i]/=10;
                }
                dq.push_front(nums[i]);

            }
            
            else
            {
                dq.push_front(nums[i]);
            }
            

        }
        vector<int>ans(dq.begin(),dq.end());
        return ans;
    }
};