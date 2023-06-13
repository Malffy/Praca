#include <stdio.h>
#include <stdlib.h>

int suma_cyfr(int a)
{
    if (a < 0 || a > 10000)
    {
        return -1;
    }
    if (a == 0)
    {
        return 0;
    }
    else
    {
        return (a % 10) + suma_cyfr(a/10);
    }
}

int main(){
    printf("suma cyfr dla 1234: %i\n", suma_cyfr(1234));
    printf("suma cyfr dla 0: %i\n", suma_cyfr(0));
}
