#include <iostream>
#include <vector> 

using namespace std;

int main(){
    int n, k, input, sum=0;
    vector <int> v;
    cin >> n >> k;
    for (int i=0; i<n; i++){
        cin >> input;
        v.push_back(input);
    }
    for (int j=0; j<n; j++){
        if(v[j]>=v[k-1] && v[j]>0){
            sum++;
        }
    }
    cout << sum << endl;
    return 0;
}