#include <stdio.h>
#include <stdlib.h>

double* nowy_blok_double(int n)
{
    return (double*)malloc(sizeof(double)*n);
}

int main()
{
    double* bl = nowy_blok_double(5);

    bl[0] = 2.2;
    bl[1] = 5.5;
    bl[2] = 10.243;
    bl[3] = 45.34;

    printf("%f, %f, %f, %f", bl[0], bl[1], bl[2], bl[3]);
}
