class Solution {
public:
    int pivotInteger(int n) {
        int tot=((n)*(n+1))/2;
      int ans=sqrt(((n)*(n+1))/2);
      if(ans*ans==tot){
        return ans;
      }
      return -1;
      
    }
};