#include <stdio.h>

int main() {
    int input;
    scanf("%d", &input);
    //윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
    if (input % 4 == 0 && (input % 100 != 0 || input % 400 == 0))
        printf("1");
    else
        printf("0");
    return 0;
}