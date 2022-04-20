#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int binary(int a[],int l,int e)
{
    int  s=0;
    int end;
    end = l-1;

    while(s<=end)
    {

        int mid = s + (end-s)/2;

        if (e== a[mid]){

            return mid;
        }
        else if(a[mid]>e){
            end=mid-1;

        }
        else{
            s= mid+1;
        }
    }

    return -1;
}

int main() {
    int m,n,k,i;

    cin>>m>>n;
    cin>>k;

    int arr[100][100];

    for (i=0; i<m;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }


    for (i=0; i<n;i++){
        if (arr[n-1][0]<=k){
            i = n-1;
            break;
        }
        else if (arr[i][0]<=k && arr[i+1][0]>k){
            break;
        }
    }
    //cout<<i<<"\n";

    int y = binary(arr[i],m,k);

    if (y == -1){
        cout<<"False";
    }
    else{
        cout<<"True\n";
        cout<< i<<" "<<y;
    }

}

