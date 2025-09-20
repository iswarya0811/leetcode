class Solution {
public:
#define p pair<int,int>
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int>res;
       
        vector<int>cnt;
        for(int i=0;i<mat.size();i++)
        {
            int sum=0;
            for(int j=0;j<mat[0].size();j++)
            {
                
                if(mat[i][j]==1)
                {
                    sum++;
                    

                }
            }
            cnt.push_back(sum);
        }
        priority_queue<p,vector<p>,greater<p>>pq;
        for(int i=0;i<cnt.size();i++)
        {
            pq.push({cnt[i],i});
        }
        while(k--)
        {
            res.push_back(pq.top().second);
            pq.pop();

        }
        return res;
    }
};