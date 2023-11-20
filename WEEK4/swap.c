#include <stdio.h>
#include <cs50.h>
#include <string.h>

void swap(int *a, int *b);


int main() {
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y)
    swap(&x, &y)
    printf("x is %i, y is %i\n", x, y)

}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b
    *b = tmp;
} /* must go to the address to swap the variables as other wise you're simplying passing in the literally value copies of those variables*/