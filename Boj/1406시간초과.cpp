#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    int pos = 0;
    string input;
    cin >> input;

    cin >> n;

    vector<char> text(input.begin(), input.end());
    pos = text.size();


    for (int i = 0; i < n; i++) {
        string type;

        cin >> type;

        if (type == "L") {
                if (pos == 0){
                    continue;
                } else {            
                    pos--;
                }
        } else if (type == "D"){
            if (pos == text.size()){
                continue;
            } else {            
                pos++;
            }
        } else if (type == "B"){
            if (pos == 0){
                continue;
            } else {            
                text.erase(text.begin() + pos-- -1);
            }
        } else if (type == "P"){
            char t;
            cin >> t;
            text.insert(text.begin() + pos++ , t);
        }
    }
    string t(text.begin(), text.end());
    cout << t << endl;
}