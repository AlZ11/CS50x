#include <stdio.h>

int main() {
    int x;
    printf("x: ");
    scanf("%i", &x);
    printf("x: %i\n", x);

    char *s;
    /* won't work since we have not allocated enough memory
    instead we can do char s[4] */
    printf("s: ");
    scanf("%s", s); /* no need & since strings are already addresses*/
    printf("s: %s\n", s);
}