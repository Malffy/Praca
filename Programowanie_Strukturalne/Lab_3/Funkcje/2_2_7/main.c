#include <stdio.h>
#include <stdlib.h>

int potega(int n, int m)
{
    int w=0;
    for(int i=1;i<=m;i++)
    {
        w*=n;
    }
    return w;
}

int main()
{
    printf("%d",potega(3,2));
}
