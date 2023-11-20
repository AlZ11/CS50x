#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


int main() {
    char *s = get_string("s: ");
    if (s == NULL) [
        return 1;
    ]
    /* do this if you're trying to allocate too much memory compared to what is available */
    char *t = malloc(strlen(s) + 1);

    for (int i = 0, n = strlen(s) + 1; i < n; i++) {
        t[i] = s[i];
    }
    /* same thing as strcpy(t, s) */
    if (strlen(t) > 0) {
         t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    free(t);
    /* You should free the memory you used malloc to allocate by passing in the same address you got back */
}
