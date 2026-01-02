#include <iostream>
#include <vector>

using namespace std;

class Edge {
   public:
    int dest;
    int weight;

    Edge(const int dest, const int weight)
        : dest(dest), weight(weight) {}
};

class Node {
   public:
    vector<Edge> edge;
    int id;
};

int DFS(vector<Node>& vec, vector<bool>& checked, int node1, int node2) {
    if (checked[node1]) {
        return -1;
    }

    checked[node1] = true;

    if (node2 == vec[node1].id) {
        return 0;
    }

    Node node = vec[node1];
    for (Edge edge : node.edge) {
        int temp = DFS(vec, checked, edge.dest, node2);
        if (temp != -1) {
            return edge.weight + temp;
        }
    }

    return -1;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int m, n;
    cin >> n >> m;
    vector<Node> tree(n + 1);

    for (int i = 1; i <= n; ++i) {
        tree[i].id = i;
    }

    for (int i = 0; i < n - 1; ++i) {
        int node1, node2, weight;
        cin >> node1 >> node2 >> weight;
        tree[node1].edge.push_back(Edge(node2, weight));
        tree[node2].edge.push_back(Edge(node1, weight));
    }
    for (int i = 0; i < m; ++i) {
        int node1, node2;
        vector<bool> checked(n + 1);
        cin >> node1 >> node2;

        cout << DFS(tree, checked, node1, node2) << '\n';
    }

    return 0;
}