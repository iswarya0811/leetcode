class Solution {
public:
    string reformatDate(string date) {
        int space=date.find(' ');

        string day= date.substr(0,space-2);
        if(day.length()==1)
        {
            day = '0'+day;
        }
        string mon=date.substr(space+1,3);
        string year=date.substr(space+5,4);
        string m;
        if(mon=="Jan") { m="01"; }
        else if(mon=="Feb") { m="02"; }
        else if(mon=="Mar") { m="03"; }
        else if(mon=="Apr") { m="04"; }
        else if(mon=="May") { m="05"; }
        else if(mon=="Jun") { m="06"; }
        else if(mon=="Jul") { m="07"; }
        else if(mon=="Aug") { m="08"; }
        else if(mon=="Sep") { m="09"; }
        else if(mon=="Oct") { m="10"; }
        else if(mon=="Nov") { m="11"; }
        else if(mon=="Dec") { m="12"; }
        string ans=year+"-"+m+"-"+day;
        return ans;
    }
};