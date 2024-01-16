#include <iostream>
#include <queue>

using namespace std;

queue<int> que;

void push(int x) {
    que.push(x);
}

int pop() {
    if (que.empty()) return -1; 
    int tmp = que.front();
    que.pop();
    return tmp;
}

int size() {
    return que.size();
}
int empty() {
    return (que.empty()) ? 1 : 0;
}

int front() { 
    if (que.empty()) return -1; 
    else return que.front();
}
int back(){
    if (que.empty()) return -1; 
    else return que.back();    
}


int main(){
    int n = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        string text;
        cin >> text;
        if (text == "push") {
            int temp;
            cin >> temp;
            push(temp);
        } else if (text == "pop") {
            cout << pop() << endl;
        } else if (text == "size") {
            cout << size() << endl;
        } else if (text == "empty") {
            cout << empty() << endl;
        } else if (text == "front") {
            cout << front() << endl;
        } else if (text == "back") {
            cout << back() << endl;
        }
    }
}