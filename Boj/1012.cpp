#include <iostream>
#include <vector>

using namespace std;

class Node {
   public:
    bool value = false;
    bool checked = false;
    int cluster_id = -1;
};

void DFS(vector<vector<Node>>& vec, const int m, const int n, const int id) {
    if (vec[m][n].checked){
        return;
    }
    vec[m][n].checked = true;
    vec[m][n].cluster_id = id;

    if (m - 1 > -1 && vec[m - 1][n].value) {
        DFS(vec, m - 1, n, id);
    }
    if (n + 1 < vec[m].size() && vec[m][n + 1].value) {
        DFS(vec, m, n + 1, id);
    }
    if (m + 1 < vec.size() && vec[m + 1][n].value) {
        DFS(vec, m + 1, n, id);
    }

    if (n - 1 > -1 && vec[m][n - 1].value) {
        DFS(vec, m, n - 1, id);
    }


}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int num = 0;
    int t, m, n, k;
    cin >> t;

    while (true) {
        if (t == 0) {
            break;
        }
        num = 0;

        cin >> m >> n >> k;
        vector<vector<Node>> vec(m, vector<Node>(n));

        int tempM;
        int tempN;

        for (int i = 0; i < k; ++i) {
            cin >> tempM >> tempN;
            vec[tempM][tempN].value = true;
        }
        {
            Node temp;

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    temp = vec[i][j];
                    if (temp.value && temp.cluster_id == -1) {
                        DFS(vec, i, j, ++num);
                    }
                }
            }
        }

        cout << num << '\n';
        t--;
    }
    return 0;
}