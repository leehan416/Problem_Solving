#include <iostream>
#include <string>
#include <stack>

using namespace std;

void textOut(stack<char> &stk);

int main() {
    string input;
    bool isTag = false;
    stack<char> stk;

    getline(cin, input);

    input += ' ';

    for (int i = 0; i < input.size(); i++) {
        if (input[i] == '<') {
            textOut(stk);
            cout << input[i];
            isTag = true;
        } else if (isTag) {
            if (input[i] == '>') isTag = false;
            cout << input[i];
        } else if (input[i] == ' ') {
            textOut(stk);
            cout << input[i];
        } else {
            stk.push(input[i]);
        }
    }

    return 0;
}
void textOut(stack<char> &stk) {
    while (!stk.empty()) {
        cout << stk.top();
        stk.pop();
    }

}