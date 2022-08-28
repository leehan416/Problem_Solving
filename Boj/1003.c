#include <stdio.h>

int main(void) {
    int arr0[41] = {1, 0, 1, 1};
    int arr1[41] = {0, 1, 1, 2};
    int value, num;
    
    scanf("%d", &value);
    
    for (int i = 0; i < value; i++) {
        scanf("%d", &num);
        for (int j = 4; j <= num; j++) {
            arr0[j] = arr0[j - 1] + arr0[j - 2];
            arr1[j] = arr1[j - 1] + arr1[j - 2];
        }
        printf("%d %d\n", arr0[num], arr1[num]);
    }

    return 0;
}