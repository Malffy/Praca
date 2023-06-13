#include <stdio.h>
#include <stdlib.h>

void przypisz(int n, int* w)
{
    *w = n;
}

int main()
{
    int a = 0;

    przypisz(3, &a);

    printf("%i", a);
}
