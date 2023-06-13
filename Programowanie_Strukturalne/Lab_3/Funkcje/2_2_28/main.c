#include <stdio.h>
#include <stdlib.h>

int foo(int n,int m)
{
    if(m==0)
        return n;
    if(n<m)
        return foo(m,n);
    return n-m+foo(n-1,m)+foo(n,m-1);
}

int main()
{
    printf("%d\n",foo(1,1));
    return 0;
}
