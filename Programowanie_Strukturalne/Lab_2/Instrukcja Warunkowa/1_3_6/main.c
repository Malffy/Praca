#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a1,b1,c1,a2,b2,c2;
    int W, Wx, Wy, x, y;
    scanf("%d%d%d%d%d%d",&a1,&b1,&c1,&a2,&b2,&c2);
    W = a1 * b2 - a2 * b1;
    Wx = c1 * b2 - c2 * b1;
    Wy = a1 * c2 - a2 * c1;

    if( W != 0 )
    {
        x = Wx / W;
        y = Wy / W;
        printf( "x = %d, y = %d", x, y );
    }
    else // Gdy W=0
    {
        if( Wx == 0 && Wy == 0 )
        {
            printf( "Uklad ma nieskonczenie wiele rozwiazan!" );
        }
        else
        {
            printf( "Uklad nie ma rozwiazan!" );
        }
    }
    return 0;
}
