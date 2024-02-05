#include <iostream>
#include <stack>

using namespace std;

int ngf[1000001] = {0};
int F[1000001] = {0};
int arr[1000001] = {0};

int main() {
    
    stack<int> stk;
    int n;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        F[arr[i]]++;
    }

    for (int i = n - 1; i >= 0; i--) {
        while(1) {
            if (stk.empty()) {
                ngf[i] = -1;
                stk.push(arr[i]);
                break;
            } else {
                if (F[stk.top()] > F[arr[i]]){
                    ngf[i] = stk.top();
                    stk.push(arr[i]);
                    break;
                } else {
                    stk.pop(); 
                }
            }
        }

    }

    for (int i = 0; i < n; i++) {
        cout << ngf[i] << ' ';
    }
    
    return 0;
}