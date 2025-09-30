class Solution {
public:
    vector<int> evenOddBit(int n) {
        vector<int>ans(2,0);
        string s=bitset<10>(n).to_string();
        int len=s.size();
        for(int i=0;s[i]!='\0';i++)
        {
            if(s[len-i-1]=='1' )
            {
                if(i%2==0)
                ans[0]++;
                else
                ans[1]++;
            } 
           
        }
        return ans;
        
    }
};