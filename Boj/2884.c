#include <stdio.h>

int main(void) {
    int hour, min;
    scanf("%d %d", &hour, &min);
    if (min >= 45)
        min -= 45;
    else {
        if (hour < 1)
            hour = 23;
        else hour--;
        min += 15;
    }
    printf("%d %d", hour, min);
    return 0;
}