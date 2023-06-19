package pl.uwm.wmii.kaz.lemmgator;

import java.time.LocalDate;

public class Biurko extends Mebel{
    private LocalDate dataProdukcji;
    private double przekatnaMonitora;
    public Biurko(String nazwa, double dlugosc, double szerokosc, Integer iloscNog, double przekatnaMonitora) {
        super(nazwa, dlugosc, szerokosc, iloscNog);
        this.przekatnaMonitora = przekatnaMonitora;
        this.dataProdukcji = LocalDate.now();
    }

    public LocalDate getDataProdukcji() {
        return dataProdukcji;
    }

    public void setDataProdukcji(int rok, int miesiac, int dzien) {
        this.dataProdukcji = LocalDate.of(rok, miesiac, dzien);
    }

    @Override
    public String toString() {
        return super.toString() + " ["
                + this.dataProdukcji.plusYears(2)
                + "] [" + this.dataProdukcji.getDayOfWeek()
                + "] [" + this.dataProdukcji.getDayOfYear() + "]";
    }

    @Override
    public boolean equals(Object other) {
        if (!super.equals(other) || !(other instanceof Biurko)) {
            return false;
        }
        Biurko ebe = (Biurko) other;
        return this.przekatnaMonitora == ebe.przekatnaMonitora
                && this.dataProdukcji.equals(ebe.dataProdukcji);
    }
}
