#include <stdio.h>

int main() {
    int num;
    scanf("%d", &num);
    for (int i = 1; i < num + 1; i++) {
        for (int n = 0; n < num - i; n++)
            printf(" ");
        for (int n = 0; n < i; n++)printf("*");
        printf("\n");
    }
    return 0;
}
