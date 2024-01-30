#include <iostream>
#include <stack>

using namespace std;

int main() {
    string input;
    stack<int> stk;
    int num = 0;

    cin >> input;

    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '('){
            if (input[i+1] == ')') {
                num  += stk.size();
                i++;

            } else {
                stk.push(0);
            }
        } else { 
            num++;
            stk.pop();
        }
    }

    cout << num << endl;

    return 0;
}