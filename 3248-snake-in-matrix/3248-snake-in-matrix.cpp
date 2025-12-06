class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int ans=0,i=0,j=0;
        for(auto it:commands)
        {
            if(it=="DOWN")
            {
                i=i+1;
                
            }
            else if(it=="RIGHT")
            {
                j=j+1;

            }
            else if(it=="UP")
            {
                i=i-1;
            }
            else
            {
                j=j-1;
            }
            ans=(n*i)+j;

        }
        return ans;
    }
};