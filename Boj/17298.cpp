#include <iostream>
#include <stack>

using namespace std;

int main() {
    int arr[1000000];
    int nge[1000000] = {0};
    stack<int> stk;

    int n;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = n - 1; i >= 0; i--) {

        while (1) {
            if (stk.empty()) {
                nge[i] = -1;
                stk.push(arr[i]);
                break;
            } else {
                if (stk.top() > arr[i]) {
                    nge[i] = stk.top();
                    stk.push(arr[i]);
                    break;
                } else {
                    stk.pop();
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        cout << nge[i] << " ";        
    } 
    return 0;
}