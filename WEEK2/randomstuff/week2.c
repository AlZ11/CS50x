#include <stdio.h>
#include <cs50.h>

const int N = 3;

float average(int x[]) {
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += x[i];
    }
    return sum / (float) N;
}

int main () {
    int score[N];
    for (int i = 0; i < N; i++) {
        score[i] = get_int("Score: ");
    }

    printf("Average: %f\n", average(score));
}
