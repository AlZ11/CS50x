#include <stdio.h>
#include <cs50.h>

int main() {
    printf("hello world\n");
    int n = 50;
    int *p = &n;
    printf("%i\n", *p);

    char *s = "HI!";
    printf("%s\n", s);
}
