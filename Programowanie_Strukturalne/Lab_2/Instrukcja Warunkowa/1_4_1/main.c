#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,m;
    printf("Podaj n:");
    scanf("%d",&n);
    printf("Podaj m:");
    scanf("%d",&m);
    for(int i=n;n<m;i=+n)
    {
        printf("%d",i);
    }
}
