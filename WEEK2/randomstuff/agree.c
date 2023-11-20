#include <cs50.h>
#include <stdio.h>
#include <string.h>


int main() {
    int n = strlen(input);
    string binaries[n];
    binaries[j] = "01001000";
    binaries[1] = "01001001";
   int x = (binaries[0] [0]) - 48;
   printf("%i\n", x);
}

string binaries(string input) {
    int n = strlen(input);
    string binary[n];
    for (int j = 0; j < n; j++) {
        binary[j] = 0;
        for (int i = 0; i < n; i++) {
        if (input[i] >= 127) {
            binary[j] += 10000000;
            input[i] -= 128;
        } if (input[i] >= 64) {
            binary[j] += 1000000;
            input[i] -= 64;
        } if (input[i] >= 32) {
            binary[j] += 100000;
            input[i] -= 32;
        } if (input[i] >= 16) {
            binary[j] += 10000;
            input[i] -= 16;
        } if (input[i] >= 8) {
            binary[j] += 1000;
            input[i] -= 8;
        } if (input[i] >= 4) {
            binary[j] += 100;
            input[i] -= 4;
        } if (input[i] >= 2) {
            binary[j] += 10;
            input[i] -= 2;
        } if (input[i] >= 1) {
            binary[j] += 10;
            input[i] -= 1;
        }
        }
    } return binary;
}










/*int convert_binary(string input) {
    for (int i = 0, n = strlen(input); i < n; i++) {
        int x = input[i];
        for (int j = 7; j > 0; j--) {
            if (x % pow(2, n) < x) {

        }

        }

    } return binary;
}*/