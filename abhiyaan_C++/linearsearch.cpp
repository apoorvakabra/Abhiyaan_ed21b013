#include <iostream>

#include <bits/stdc++.h>
using namespace std;

int main() {
    int m,n,k;

    cin>>m>>n;
    cin>>k;

    int arr[100][100];

    for (int i=0; i<m;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }
    int f=0;

    for (int i=0; i<m;i++){
        for(int j=0;j<n;j++){
            if (arr[i][j]==k){
                cout<<"True\n";
                cout<<i<<" "<<j;
                f=1;
            }
        }
    }
    if (f==0){
        cout<<"False";
    }
}

