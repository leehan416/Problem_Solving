#include <iostream>
#include <stack>

using namespace std;

int main() {
    int n;

    stack<char> stk1, stk2;

    string input;
    cin >> input;

    for (int i = 0; i < input.size(); i++)
        stk1.push(input[i]);

    cin >> n;

    for (int i = 0; i < n; i++) {
        string type;

        cin >> type;

        if (type == "L") {
            if (stk1.empty())
                continue;
            else {
                stk2.push(stk1.top());
                stk1.pop();
            }
        } else if (type == "D"){
            if (stk2.empty()){
                continue;
            } else {
                stk1.push(stk2.top());
                stk2.pop();
            }
        } else if (type == "B"){
             if (stk1.empty()){
                continue;
             } else {
                stk1.pop();
             }
        } else if (type == "P"){
            char t;
            cin >> t;
            stk1.push(t);    
        }
    }

    while (!stk1.empty()){
        stk2.push(stk1.top());
        stk1.pop();
    }

    while (!stk2.empty()) {
        cout << stk2.top();
        stk2.pop();    
    }
}