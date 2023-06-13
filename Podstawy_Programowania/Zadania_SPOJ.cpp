#include <vector>
#include <iostream>
using namespace std;

int odleglosc_domu(vector<int>tab, int nrDomu)
{
    int wynik = 0;
    for (int i = 0; i < tab.size(); i++)
    {
        int temp = nrDomu - tab[i];
        temp = abs(temp);
        wynik += temp;
    }
    return wynik;
}

int najlepszy_dom(vector<int>tab)
{
    int wynik = tab[0];
    int odleglosc = odleglosc_domu(tab, tab[0]);
    for (int i = 0; i < tab.size(); i++)
    {
        int temp_odl = odleglosc_domu(tab, tab[i]);

        if (temp_odl < odleglosc)
        {
            odleglosc = temp_odl;
            wynik = tab[i];
        }
    }
    return wynik;
}

int suma_odleglosc(vector<int>tab)
{
    vector<int>sumy;
    int index=0;
    int suma=0;
    for (int i = 0; i < tab.size(); i++)
    {
            for (int i = 0; i < tab.size(); i++)
            {
                index++;
                if (tab[i] != 0)
                {
                    suma += index;
                }
                sumy.push_back(suma);
            }
    }
    return min(sumy);
}






int main()
{
    vector<int>tab = { 1,0,3,4,5,0,0,8,3 };
    cout << odleglosc_domu(tab,5);
}
