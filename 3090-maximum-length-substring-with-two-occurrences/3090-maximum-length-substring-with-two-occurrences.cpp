class Solution {
public:
    int maximumLengthSubstring(string s) {
        vector<int>mp(256,0);
        int l=0,r=0,maxlength=0;
        for(int i=0;i<s.size();i++)
        {
               mp[s[i]]++;
            while(mp[s[i]]>2)
            {
                mp[s[l]]--;
                l++;
            }
         
        
            maxlength=max(i-l+1,maxlength);
               

        }
        return maxlength;
        
    }
};