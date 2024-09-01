#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int num = 0;
    int ab = b - a;
    int cb = c - b;
    num = (ab > cb)? ab -1: cb -1;
    cout << num << endl;
    return 0;
}