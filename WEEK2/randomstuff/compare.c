#include <stdio.h>
#include <cs50.h>

int main()
{
    int x = get_int("What is x? ");
    int y = get_int("What is y? ");

    if (x<y) {
        printf("X is less than Y\n");
    } else if (x>y) {
        printf("X is greater than Y\n");
    } else {
        printf("X is equal to Y\n");
    }
}