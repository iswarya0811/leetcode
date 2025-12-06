class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int m=image.size();
        int n=image[0].size();
        
        vector<vector<int>>inverted(m,vector<int>(n));
        for(int i=0;i<image.size();i++)
        {
            int k=0;
            for(int j=image[0].size()-1;j>=0;j--)
            {
                inverted[i][k++]=1-image[i][j];

            }
        }
        return inverted;
    }
};