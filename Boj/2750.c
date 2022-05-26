#include<stdio.h>

int main() {

    int input, i, k;
    scanf("%d", &input);

    int list[input];

    for (i = 0; i < input; i++) {
        int set;
        scanf("%d", &set);
        list[i] = set;
    }


    for (i = 0; i < input; i++) {
        for (k = 0; k < (input - 1) - i; k++) {
            if (list[k] > list[k + 1]) {
                int temp = list[k];
                list[k] = list[k + 1];
                list[k + 1] = temp;
            }
        }
    }

    for (i = 0; i < input; i++)
        printf("%d\n", list[i]);
    return 0;
}