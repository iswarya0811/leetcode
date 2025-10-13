class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int>mpp(256,-1);
        int l=0,r=0;
        int maxlen=0;
        int n=s.size();
        if(n==0)
        {
            return 0;
        }
        while(r<n)
        {
            if(mpp[s[r]]!=-1)
            {
                if(mpp[s[r]]>=l)
                {
                    l=mpp[s[r]]+1;
                }
            }
        mpp[s[r]]=r;
            maxlen=max(maxlen,r-l+1);
           
            r++;
        }
        return maxlen;
    }
};