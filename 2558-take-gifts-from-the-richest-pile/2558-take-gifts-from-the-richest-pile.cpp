class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        long long sum=0;
        priority_queue<long long>pq;
        for(int i=0 ;i<gifts.size();i++)
        {
            pq.push(gifts[i]);
        }
        while(k--)
        {
            int a=pq.top();
            pq.pop();
            pq.push(floor(sqrt(a)));
        }
        while(!pq.empty())
        {
            sum+=pq.top();
            pq.pop();
        }
        return sum;
        
    }
};