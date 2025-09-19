class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int rows=grid.size();
        int cols=grid[0].size();
        vector<int>res;
       if(rows<3 || cols<3) return 0;
        int sum;
    
        for(int i=0;i<=rows-3;i++){
            for(int j=0;j<=cols-3;j++)
            {
                sum=0;
                sum=grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]+grid[i+1][j+1];
                res.push_back(sum);
            }
        }
        return *max_element(res.begin(),res.end());
        
    }
};