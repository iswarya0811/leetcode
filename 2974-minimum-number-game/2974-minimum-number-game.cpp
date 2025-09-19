class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        vector<int>res(nums.size());
        priority_queue<int,vector<int>,greater<int>> pq;
        for(int i=0;i<nums.size();i++){
            pq.push(nums[i]);
        }
        
        for(int i=1;i<nums.size();i+=2){
        res[i]=pq.top();
        pq.pop();
        res[i-1]=pq.top();
        pq.pop();
        }
        return res;

    }
};