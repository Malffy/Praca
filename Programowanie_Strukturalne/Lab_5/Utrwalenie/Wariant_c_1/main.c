#include <stdio.h>
#include <stdlib.h>

double f1(double a)
{
    return a;
}
double f2(double a)
{
    return a*a*a;
}

double f3(double a)
{
    return a*a;
}

int funkcja(double (*funkcja1)(double), double(*funkcja2)(double), double x)
{
    if (x < 1)
    {
        return -1;
    }
    else
    {
        for (int i = 0; ++i <= x;)
        {
            double r = funkcja1(i);
            r*=r*r;
            //printf("i = %i, r = %f\n", i, r);
            if (funkcja2(i) != r)
            {
                return -1;
            }
        }
        return 1;
    }
}

int main()
{
    printf("Prawda : funkcja zwraca %i\n", funkcja(&f1, &f2, 5));
    printf("Falsz : funkcja zwraca %i\n", funkcja(&f1, &f3, 5));
    return 0;
}
