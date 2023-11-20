#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string passage = get_string("Text: ");
    float letter = count_letters(passage);
    float word = count_words(passage);
    float sentence = count_sentences(passage);
    printf("%i letters\n", count_letters(passage));
    printf("%i words\n", count_words(passage));
    printf("%i sentences\n", count_sentences(passage));
    float L = (letter / word) * 100;
    float S = (sentence / word) * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string passage)
{
    int letter = 0;
    int n = strlen(passage);
    for (int i = 0; i < n; i++)
    {
        if (passage[i] >= 'a' && passage[i] <= 'z')
        {
            letter++;
        }
        if (passage[i] >= 'A' && passage[i] <= 'Z')
        {
            letter++;
        }
    }
    return letter;
}

int count_words(string passage)
{
    int word = 0;
    int n = strlen(passage);
    for (int i = 0; i < n; i++)
    {
        if (passage[i] == ' ')
        {
            word++;
        }
    }
    return word + 1;
}

int count_sentences(string passage)
{
    int sentence = 0;
    int n = strlen(passage);
    for (int i = 0; i < n; i++)
    {
        if (passage[i] == '.' || passage[i] == '!' || passage[i] == '?')
        {
            sentence++;
        }
    }
    return sentence;
}
