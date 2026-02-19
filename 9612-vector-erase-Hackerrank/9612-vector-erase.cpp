#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin >> n;
    vector<int>arr(n);
    for(int &i:arr)
    {
        cin >> i;
    } 
    int key;
    cin >> key;
    int a,b;
    cin >> a >> b;
    arr.erase(arr.begin()+key-1);
    arr.erase(arr.begin()+a-1,arr.begin()+b-1);
    cout << arr.size() << endl;
    for(int i : arr)
    {
        cout << i << " ";
    }
     
    return 0;
}
