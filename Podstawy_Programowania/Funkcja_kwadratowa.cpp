#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double a=2, b=8, c=-10, delta, x1, x2;
    if(a!=0)
    {
        delta = (b * b) - 4 * (a * c);
        cout << delta<<"\n";

        if (delta < 0 )
        {
            cout << "Delta jest ujemna, funkcja kwadratowa nie ma pierwiastkow.";
        }
        if (delta > 0)
        {
            x1 = ((-b) - sqrt(delta)) / (2 * a);
            x2 = ((-b) + sqrt(delta)) / (2 * a);
            cout << "Delta jest wieksza od 0, x1=" << x1 << ", x2=" << x2;
        }
        if (delta == 0)
        {
            x1 = (-b) / (2 * a);
            cout << "Delta jest rowna 0 , x1=" << x1;
        }
    }
    else
    {
        cout << "To nie funkcja kwadratowa!";
    }
}
