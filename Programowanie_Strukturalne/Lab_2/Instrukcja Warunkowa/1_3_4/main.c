#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    if(abs(a)>abs(b))
    {
        printf("%d",a);
    }
    else
    {
        printf("%d",b);
    }
    return 0;
}
