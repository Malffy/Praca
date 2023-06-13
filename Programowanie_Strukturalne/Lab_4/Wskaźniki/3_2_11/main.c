#include <stdio.h>
#include <stdlib.h>

int* nowy_blok_int(int n)
{
    return (int*)malloc(sizeof(int)*n);
}

int main()
{
    int* bl = nowy_blok_int(5);

    bl[0] = 2;
    bl[1] = 5;
    bl[2] = 10;
    bl[3] = 45;

    printf("%i, %i, %i, %i", bl[0], bl[1], bl[2], bl[3]);
}
