#include<iostream>

using namespace std;

int main(int argc, char** argv){
    string input;
    int arr[26] ={0};

    cin >> input;

    for (int i = 0 ; i < input.length(); ++i){
        arr[input[i]- 'a']++;
    }


    for (int i = 0 ; i < 26; ++i){
        cout << arr[i] <<" ";
    }
    cout << endl;
    return 0;
}