#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
int binary(string input);

int main(void)
{
string input = get_string("Message: ");
printf("binary: %i\n", binary(input));
for (int i = 0; i < BITS_IN_BYTE; i++) {
    int bit = binary(input)
    print_bulb(bit);
}
}

void print_bulb(int bit)
{
    printf("\U000026AB");

    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}


string binary(string input) {
    int binary = 0;
        for (int i = 0; i < strlen(input); i++) {
        if (input[i] >= 127) {
            binary += 10000000;
            input[i] -= 128;
        } if (input[i] >= 64) {
            binary += 1000000;
            input[i] -= 64;
        } if (input[i] >= 32) {
            binary += 100000;
            input[i] -= 32;
        } if (input[i] >= 16) {
            binary += 10000;
            input[i] -= 16;
        } if (input[i] >= 8) {
            binary += 1000;
            input[i] -= 8;
        } if (input[i] >= 4) {
            binary += 100;
            input[i] -= 4;
        } if (input[i] >= 2) {
            binary += 10;
            input[i] -= 2;
        } if (input[i] >= 1) {
            binary += 10;
            input[i] -= 1;
        }
        } return binary;
}