package pl.uwm.wmii.kaz.lemmgator;

import java.time.LocalDate;
import java.util.Objects;

public class Court {
    private double width;
    private double length;
    private String address;
    private int year_built;

    public Court(double width, double length, String address, int year_built) {
        if (width < 45 || width > 90 || length < 90 || length > 120) {
            this.width = 68;
            this.length = 100;
        } else {
            this.width = width;
            this.length = length;
        }
        this.address = address;
        this.year_built = year_built;
    }

    public Court(String address, int year_built) {
        this(68, 100, address, year_built);
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        if (width < 45 || width > 90) {
            this.width = 68;
        } else {
            this.width = width;
        }
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        if (length < 90 || length > 120) {
            this.length = 100;
        } else {
            this.length = length;
        }
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getYear_built() {
        return year_built;
    }

    public void setYear_built(int year_built) {
        this.year_built = year_built;
    }

    public static void validate(Court court) {
        int now = LocalDate.now().getYear();
        if (court.year_built < 0 || court.year_built > now) {
            court.year_built = now;
        }
    }

    public double area() {
        return getWidth() * getLength();
    }

    @Override
    public String toString() {
        return "Boisko wybudowane w roku " + this.year_built + ", o dlugosci " + this.length + " metrow i szerokosci " + this.width + " metrow.\n" +
                "Pole powierzchni: " + area() + " mkw.\n" +
                "Adres: " + this.address + ".";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null) return false;
        if (!(o instanceof Court court)) return false;
        return Double.compare(court.width, width) == 0 && Double.compare(court.length, length) == 0;
    }
}