#include <stdio.h>

int main(void) {
    int num;
    int value[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &num);
        value[i] = num % 42;
    }
    num = 0;
    for (int i = 0; i < 10; i++) {
        int val = 0;
        for (int j = i + 1; j < 10; j++)
            if (value[i] == value[j]) val++;
        if (val == 0) num++;
    }
    printf("%d", num);
    return 0;
}