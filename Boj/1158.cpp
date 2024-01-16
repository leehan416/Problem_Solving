#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n, k;
    queue<int> circle;

    cin >> n;
    cin >> k;

    for (int i = 1; i <= n; i++)
        circle.push(i);

    cout << "<";

    while (1){
        for (int i = 0; i < k - 1; i++){
            circle.push(circle.front());
            circle.pop();
        }
        cout << circle.front();
        circle.pop();

        if (circle.empty()){
            break;
        } else {
            cout << ", ";
        }
    }
    cout << ">" << endl;
}