#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int m, n;

    int pack, per;

    int perMin = 9999;
    int packMin = 9999;

    int buyPack = 0;
    int buyPer = 0;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> pack >> per;
        if (pack < packMin) packMin = pack;
        if (per < perMin) perMin = per;
    }

    if (perMin * 6 < packMin) {
        buyPer = n;
    } else {
        buyPack = n / 6;
        buyPer = n % 6;
        if (buyPer * perMin > packMin) {
            buyPack++;
            buyPer = 0;
        }
    }

    cout << (buyPack * packMin) + (buyPer * perMin) << '\n';
    return 0;
}
