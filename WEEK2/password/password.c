// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);


int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password)==true)
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password) {
    int n = strlen(password);

    bool lowerCase = 0, upperCase = 0, specialCharacter = 0, number = 0;

    for (int i = 0; i < n; i++) {
        if (password[i] >= 'a' && password[i] <= 'z') {
            lowerCase = 1;
        }
        if (password[i] >= 'A' && password[i] <= 'Z') {
            upperCase = 1;
        }
        if (password[i] >= '!' && password[i] <= '/') {
            specialCharacter = 1;
        }
        if (password[i] >= '0' && password[i] <= '9') {
            number = 1;
        }
    }
    return (lowerCase && upperCase && specialCharacter && number);
}


