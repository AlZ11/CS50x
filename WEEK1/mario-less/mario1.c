#include <cs50.h>
#include <stdio.h>

int main(void) {
int tall;
int i;
int j;
int n = 0;
do {
    tall = get_int("Height: ");
 } while (tall<=0 || tall>8);


//printing how many rows
for (i=0; i<tall; i++)
{ //printing how many columns
if (n<tall) {
    n++;
}
    for (j=0; j<n; j++) {
         printf("#");
    } printf("\n");
}
 }
