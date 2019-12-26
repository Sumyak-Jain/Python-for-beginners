#include<iostream>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int a = 0; a < t; a++){
         int n;
        cin >> n;
        long int s1=(n*(n+1))/2;
        s1=s1*s1;
        long int s2;
        s2=n*(n+1);
        int a1=2*n+1;
        s2=s2*a1;
        s2=s2/6;
        cout<<s1-s2<<endl;
        
    }
    return 0;
}
