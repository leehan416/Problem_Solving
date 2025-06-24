#include<iostream>

using namespace std;

int main (){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    int temp;
    for (int i = 0; i < n; ++i) {
        cin >> temp;
        if (temp < x) cout << temp << " ";
    }
    cout << "\n";

    
    return 0;
}