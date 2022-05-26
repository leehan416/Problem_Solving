#include <stdio.h>

int main(void) {
    int num[5];
    int value = 0;
    scanf("%d %d %d %d %d", &num[0], &num[1], &num[2], &num[3], &num[4]);
    for (int i = 0; i < 5; i++)
        value += num[i] * num[i];
    printf("%d", value % 10);
    return 0;
}