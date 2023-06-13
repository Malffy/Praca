#include <stdio.h>
#include <stdlib.h>

int WarBez(int a)
{
    if(a<0)
    return a*(-1);
}

int main()
{
    int a;
    scanf("%d",&a);
    printf("%d",WarBez(a));
    return 0;
}
