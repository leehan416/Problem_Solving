#include<stdio.h>

int main() {
    int arrayNum;

    scanf("%d", &arrayNum);
    int array[arrayNum][10];
    for (int i = 0; i < arrayNum; i++) {
        scanf("%d %d %d %d %d %d %d %d %d %d", &array[i][0], &array[i][1], &array[i][2], &array[i][3], &array[i][4],
              &array[i][5], &array[i][6], &array[i][7], &array[i][8], &array[i][9]);
    }
    for (int i = 0; i < arrayNum; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 9-j; k++) {
                if (array[i][k] < array[i][k + 1]) {
                    int temp = array[i][k];
                    array[i][k] = array[i][k + 1];
                    array[i][k + 1] = temp;
                }
            }
        }
    }
    for (int i = 0; i < arrayNum; i++) {
        printf("%d\n", array[i][2]);
    }
    return 0;
}