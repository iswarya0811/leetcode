class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        vector<int>a;
        int cnt=0,prev,curr,diff;
       
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='1') {
                a.push_back(i);
                cnt++;
            }
        }
        if (cnt < k) return "";
        int min=INT_MAX;
        for(int i=0;i<=cnt-k;i++)
        {
           diff= a[i+k-1]-a[i];
           if(diff <= min)
           {
            prev=a[i];
            curr=a[i+k-1];
            min=diff;
           }
        }
        return s.substr(prev,curr-prev+1);
        
       
    }
};