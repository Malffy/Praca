#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    unsigned int n,a=0,w=0;
    scanf("%u",&n);
    for(int i=0; i<=n; i++)
    {
        a=pow(i,2);
        w+=a;
    }
    printf("%u",w);
    return 0;
}

