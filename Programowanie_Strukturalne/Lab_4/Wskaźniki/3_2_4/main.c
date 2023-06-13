#include <stdio.h>
#include <stdlib.h>

void sort(int* a, int* b)
{
    if (*a > *b)
    {
        int t = *a;
        *a = *b;
        *b = t;
    }
}

int main()
{
    int a = 4;
    int b = 2;


    printf("%i, %i\n", a, b);

    sort(&a, &b);

    printf("%i, %i\n", a, b);
}
