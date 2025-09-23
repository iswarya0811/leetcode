class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
    vector<int>alpha(27,0);
    int flage;
        for(char c : allowed)
        {
            alpha[c-'a']=1;
        }
        int cnt=0;
        for(int i=0;i<words.size();i++)
        {
            flage=1;
            for(int j=0;j<words[i].size();j++)
            {
                if(alpha[words[i][j]-'a']==0)
                {
                    flage=0;
                    break;
                }
            }
            if(flage)
            cnt++;
           
        }
        return cnt;

    }
};