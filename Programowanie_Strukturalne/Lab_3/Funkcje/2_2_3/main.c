#include <stdio.h>
#include <stdlib.h>


int foo(int n)
{
   for(int k=(n-1); k>=0; k--)
    {
        if(n%k==0)
        {
        return k;
        }
    }
    return 0;
}
int main()
{
    int n;
    printf("Wpisz liczbe calkowita wieksza od 2.\n");
    scanf("%d",n);
    if(n<=2)
    {
        printf("Wpisano niepoprawna wartosc");
    }
    else
    {
        printf("%i",foo(n));
    }

    return 0;
}
