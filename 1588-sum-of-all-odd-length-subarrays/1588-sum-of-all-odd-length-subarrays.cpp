class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum=0;
        for(int i=0;i<arr.size();i++)
        {
           int count=(i+1)*(arr.size()-i);
           int contribution=(count+1)/2;
           sum+=contribution*arr[i];
        }
        return sum;
    }
};