#include <stdio.h>
#include <stdlib.h>

int mn(int* a, int* b)
{
    return *a > *b ? *b : *a;
}

int main()
{
    int a = 2;
    int b = 4;

    printf("%i", mn(&a,&b));
}
