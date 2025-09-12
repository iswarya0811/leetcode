class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int g_cnt=0,p_cnt=0,m_cnt=0,ans;
        int last_g=0,last_p=0,last_m=0;
        vector<int>prefix(garbage.size());
        prefix[0]=0;
        for(int i=1;i<garbage.size();i++){
            prefix[i]=travel[i-1]+prefix[i-1];
        }
        for(int i=0;i<garbage.size();i++){
            for(int j=0;j<garbage[i].size();j++){
                if(garbage[i][j]=='G')
                {g_cnt++;
                last_g=i;
                }
                else if(garbage[i][j]=='P')
                {
                p_cnt++;
                last_p=i;
                }
                else if(garbage[i][j]=='M'){
                m_cnt++;
                last_m=i;
                }

            }
        }
        ans= (p_cnt)+prefix[last_p]+(g_cnt)+prefix[last_g]+(m_cnt)+prefix[last_m];
        return ans;


    }
};