#include <stdio.h>
#include <stdlib.h>

void przepisz(const int* a, int* const b)
{
    *b = *a;
}

int main()
{
    const int st = 4;
    int b = 2;

    przepisz(&st, &b);

    printf("%i, %i", st, b);
}
