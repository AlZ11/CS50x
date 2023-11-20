#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string argv);

int main(int argc, string argv[])
{
    if (argc < 2) {
        printf("Error, missing command line argument\n");
    } else {
        printf("%s\n", replace(argv[1]));
    }
}

string replace(string word) {
    int n = strlen(word);
    for (int i = 0; i < n; i++) {
        switch (word[i]) {
            case 'a':
            word[i] = '@';
            break;

            case 'e':
            word[i] = '3';
            break;

            case 'i':
            word[i] = '1';
            break;

            case 'o':
            word[i] = '0';
            break;

        }
    } return word ;
}