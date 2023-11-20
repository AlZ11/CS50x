#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startSize;
    int endSize;
    int n = 0;
    int i;
    do
    {
        startSize = get_int("Start size: ");
    }
    while (startSize < 9);
    // TODO: Prompt for end size
    do
    {
        endSize = get_int("End size: ");
    }
    while (endSize < startSize);
    // TODO: Calculate number of years until we reach threshold
    for (i = startSize; endSize > i; n++)
    {
        i = i + (i / 3) - (i / 4);
    }
    // TODO: Print number of years
    printf("Years: %i\n", n);
}
