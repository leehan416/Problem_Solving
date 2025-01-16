#include <iostream>

using namespace std;

int main() {
    int n;
    int size[6];
    int t, p;
    int temp = 0;

    cin >> n;
    for (int i = 0; i < 6; i++)
        cin >> size[i];

    cin >> t >> p;

    for (int i = 0; i < 6; i++){
        if (t < size[i]) {
            if (size[i] % t) temp ++;
            temp += size[i] / t - 1;
        }
        if (0 < size[i]) temp ++;
    }

    cout << temp << endl << n / p << " " << n % p << endl;

    return 0;
}