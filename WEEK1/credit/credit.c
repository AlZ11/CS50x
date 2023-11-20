#include <cs50.h>
#include <stdio.h>

int main(void)
{
int num, n, k;
// Prompting for credit card number
    num = get_int("Number: ");
// Checksum
// Multiplying every other digit by 2
    for (n=100; n < num; n*=100) {
 k = (num % n) * 2;
printf("%i\n", k); } printf("\n");


// Add the products together
// Sum the digits that weren’t multiplied by 2
// Add both sums together
// Check whether last digit of final sum = 0
// Output Invalid/Type of card
}
