#include <iostream>
#include <deque>

using namespace std;

int main() {
    int n;
    
    deque<int> dp;
    
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string input;

        cin >> input;

        if (input == "push_front") {
            int x;
            cin >> x;
            dp.push_front(x);
        } else if (input == "push_back") {
            int x;
            cin >> x;
            dp.push_back(x);
        } else if (input == "pop_front") {
            if (dp.empty()) cout << -1 << endl;
            else {
                cout << dp.front() << endl;
                dp.pop_front();
            }
        } else if (input == "pop_back") {
            if (dp.empty())  cout << -1 << endl;
            else {
                cout << dp.back()<< endl;
                dp.pop_back();
            }
        } else if (input == "size") cout << dp.size() << endl;
        
        else if (input == "empty")  cout << dp.empty() << endl;
       
        else if (input == "front") {
            if (dp.empty())  cout << -1 << endl;
            else cout << dp.front() << endl; 
        }  else if (input == "back") {
            if (dp.empty())  cout << -1 << endl; 
            else cout << dp.back() << endl;
        }
    }
}