#include <stdio.h>
#include <stdlib.h>


int main()
{
    double a,h,P;
    printf("Wybierz: 1-TROJKAT 2-KWADRAT 3-PROSTOKAT\n");
    scanf("%lf",&a);
    if(a==1)
    {
        printf("Podaj podstawe i wysokosc trojkata\n");
        scanf("%lf%lf",&a,&h);
        P=(a*h)/2;
        printf("Pole=%lf",P);
    }
    if(a==2)
    {
        printf("Podaj bok kwadratu\n");
        scanf("%lf",&a);
        P=a*a;
        printf("Pole=%lf",P);
    }
    if(a==3)
    {
        printf("Podaj wymiary prostokatu\n");
        scanf("%lf%lf",&a,&h);
        P=a*h;
        printf("Pole=%lf",P);
    }

    return 0;
}
