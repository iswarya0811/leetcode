class Solution {
public:
string change(string num)
    {
        string ans="";
        for(int i=0;i<num.size()-1;i++)
        {
            ans+=(num[i]+num[i+1])%10;

        }
        return ans;

    }

    bool hasSameDigits(string s) {
        string second;
        while(s.size()>2)
        {
            second=change(s);
            s=second;
        }
        return second[0]==second[1];
        
    }
};