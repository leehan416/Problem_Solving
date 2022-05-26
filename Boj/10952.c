#include<stdio.h>

int main() {
    int num[2];
    while (1) {
        scanf("%d %d", &num[0], &num[1]);
        if (num[0] == 0 && num[1] == 0) break;
        else printf("%d\n", num[0] + num[1]);
    }
}