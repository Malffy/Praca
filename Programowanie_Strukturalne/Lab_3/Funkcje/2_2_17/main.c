#include <stdio.h>
#include <stdlib.h>

int licznik=0;
void foo()
{
    licznik++;
    printf("Liczba wyw.:%d\n",licznik);
}

int main()
{
    foo();
    foo();
    foo();
    return 0;
}
