#include <iostream>
#include <stack>

using namespace std;

int main() {

    int num = 1;
    int n;
    stack<int> s;
    string out = "";

    cin >> n;

    s.push(0);

    for (int i = 0; i < n; i++) {
        int input;

        cin >> input;

        while (s.top() < input) {
            s.push(num++);
            out += "+\n";
        }
        if (s.top() == input) {
            s.pop();
            out += "-\n";
        } else {
            out = "NO";
            break;
        }
    }
    cout << out;
}