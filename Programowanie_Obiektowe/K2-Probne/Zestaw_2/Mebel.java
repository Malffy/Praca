package pl.uwm.wmii.kaz.lemmgator;

public class Mebel {
    private String nazwa;
    private double dlugosc;
    private double szerokosc;
    private Integer iloscNog;
    private static int ile;

    public Mebel(String nazwa, double dlugosc, double szerokosc, Integer iloscNog){
        this.nazwa = nazwa;
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.iloscNog = iloscNog;
        ile++;
    }

    public Mebel(double dlugosc, double szerokosc, Integer iloscNog){
        this("Jakis Mebel", dlugosc, szerokosc, iloscNog);
    }

    public String getNazwa() {
        return nazwa;
    }

    public double getDlugosc() {
        return dlugosc;
    }

    public double getSzerokosc() {
        return szerokosc;
    }

    public Integer getIloscNog() {
        return iloscNog;
    }

    public static int getIle() {
        return ile;
    }

    @Override
    public String toString() {
        String x = this.getClass().getSimpleName();
        if(this.nazwa == "Jakis Mebel") {
            return x + " [" + dlugosc + "] ["
                    + szerokosc + "] ["
                    + iloscNog + "] ["
                    + ile + "]";
        }
        else {
            return x + " [" + nazwa + "] ["
                    + dlugosc + "] ["
                    + szerokosc + "] ["
                    + iloscNog + "] ["
                    + ile + "]";
        }
    }

    @Override
    public boolean equals(Object other) {
        Mebel ebe = (Mebel) other;
        if (other == this) {
            return true;
        }
        if (!(other instanceof Mebel)) {
            return false;
        }
        return this.nazwa.equals(ebe.nazwa)
                && this.dlugosc == ebe.dlugosc
                && this.szerokosc == ebe.szerokosc
                && this.iloscNog.equals(ebe.iloscNog);
    }
}
