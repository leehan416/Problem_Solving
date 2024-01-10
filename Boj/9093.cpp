#include <iostream>
#include <stack>

using namespace std;

int main() {
  int n;

  cin >> n;

  cin.ignore();

  for (int i = 0; i < n; i++) {
        string str;
        getline(cin, str);

        stack<char> s;

        for (int j = 0; j < str.size(); j++) {
            if (str[j] == ' ') {
                while (s.size()) {
                    cout << s.top();
                    s.pop();
                }
                cout << ' ';
            } else if (str[j] == '\0') {
                break;
            } else {
                s.push(str[j]);
            }


        } 
        while (s.size()) {
            cout << s.top();
            s.pop();
        }
        cout << '\n';
    }
}