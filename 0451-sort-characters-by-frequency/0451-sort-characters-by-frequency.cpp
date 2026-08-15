class Solution {
public:
#define p pair<int,char>
    string frequencySort(string s) {
        map<char,int>freq;
        for(auto ch : s)
        {
            freq[ch]++;
        }
        priority_queue<p>pq;
        for(auto i : freq)
        {
            pq.push({i.second,i.first});
        }
        string str = "";
        while(!pq.empty())
        {
            str+=string(pq.top().first,pq.top().second);
            pq.pop();

        }
        return str;

    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna