class Solution {
public:
#define p pair<int,int>
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {

        priority_queue<p,vector<p>,greater<p>> pq;
        for(int i=0;i<nums.size();i++){
            pq.push({nums[i],i});

        }
        while(k--){
            p curr=pq.top();
            pq.pop();
            int value = curr.first;
            int index = curr.second;
            nums[index]*=multiplier;
            pq.push({nums[index],index});
        }
        return nums;

        
    }
};