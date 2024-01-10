#include <iostream>

using namespace std;

int main() {
    int m;

    cin >> m;

    for (int i = 0; i < m; i++) {
        string str;
        cin >> str;
        int n = 0;
        for (int i = 0 ; i < str.size(); i++) {
            if (str[i] == '(') n++;
            else n--;
            if (n < 0) break;
        }
        if (n == 0) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}