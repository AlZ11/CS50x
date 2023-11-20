#include <stdio.h>
#include <cs50.h>
#include <string.h>

string replace(string argv);


int main() {
string word = get_string("What is the word: ");
int n = strlen(word);

    for (int i = 0; i < n; i++) {
        switch (word[i]) {
            case 1:
            if (word[i]=='a' || word[i]=='A') {
                word[i] = '@';
            } else {
               break;
            }

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
    }

printf("%s\n", word);
}
