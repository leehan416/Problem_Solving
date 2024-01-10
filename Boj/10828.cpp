#include <iostream>
#include <vector>

using namespace std;

vector<int> stack;

void push(int x) { 
    stack.push_back(x); 
}

int pop() {
    if (stack.size() == 0) 
        return -1;

    int n = stack.back();
    stack.pop_back();
    return n;
}

int size() { 
    return stack.size(); 
}

int empty() {
    if (stack.size() == 0) return 1;
    else  return 0;
}

int top() {
  if (stack.size() == 0) return -1;
  else return stack.back();
}

int main() {

    int n = 0;
    string input;
    int inputData;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> input;
        if (input == "push") {
            cin >> inputData;
            push(inputData);
        } else if (input == "pop") {
            cout << pop() << endl;
        } else if (input == "size") {
            cout << size() << endl;
        } else if (input == "empty") {
            cout << empty() << endl;
        } else if (input == "top") {
            cout << top() << endl;
        }
    }
}