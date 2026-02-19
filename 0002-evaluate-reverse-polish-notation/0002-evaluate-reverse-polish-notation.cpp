class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int>st;
        int res;
       for(auto i:tokens)
       {
        if(i == "+" || i == "-" || i=="*" || i == "/")
        {
            int b=st.top();
            st.pop();
            int a =st.top();
            st.pop();
            char op = i[0];
            switch(op){
                case '+':
                    res=a+b;
                    break;
                case '-':
                    res=a-b;
                    break;
                case '*':
                    res = a*b;
                    break;
                case '/':
                    res = a/b;
                    break;
            }
            st.push(res);
        }
        else
        {
            st.push(stoi(i));
        }
       } 
       int ans = st.top();
       return ans;
    }
};